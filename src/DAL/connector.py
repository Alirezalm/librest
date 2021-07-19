import json
import os.path

import click
import psycopg2


class DBConnector:
    def __init__(self, db_name: str = "postgres"):
        self.setting_json = os.path.join(
            os.path.abspath(os.path.dirname((os.path.dirname(os.path.dirname(__file__))))), f"config_files/{db_name}Config.json"
        )
        self.connection = None

    def _read_db_settings(self):
        with open(self.setting_json) as config_json:
            config = json.load(config_json)
        return config

    def get_connection(self):
        if self.connection is None:

            try:
                config = self._read_db_settings()
                username = config['username']
                password = config['password']
                host = config['host']
                port = config['port']
                dbname = config['dbname']
                self.connection = psycopg2.connect(
                    host = host,
                    port = port,
                    user = username,
                    password = password,
                    database = dbname
                )
                click.echo("Successfully Connected to the database")
                return self.connection
            except (Exception, psycopg2.Error) as error:
                print(error)

        else:
            click.echo("Connection Already available")
            return self.connection




