import json
import os

import click

from server.application import create_server


class FlaskManager:

    def __init__(self, config: str = "development"):
        self.config = config
        self.read_settings()

    @staticmethod
    def set_env(name: str, value: str):
        os.environ[name] = os.getenv(name, default = value)
        click.echo(f"{name} = {value}")

    def read_settings(self):
        config_json_filename = self.config + ".json"

        with open(os.path.join('config_files', config_json_filename)) as config_json_file:
            config: dict = json.load(config_json_file)

        for item, value in config.items():
            FlaskManager.set_env(item, value)

    def run_server(self, port: int):
        create_server(self.config).run(port = port)


@click.group()
def cli():
    pass


@click.command()
@click.argument("port", default = 8000)
def runserver(port):
    server_manager = FlaskManager("development")
    server_manager.run_server(port)


cli.add_command(runserver)
if __name__ == '__main__':
    cli()
