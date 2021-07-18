from flask import Flask, jsonify


def create_server(config_name: str):
    app = Flask(__name__)

    config_object = f"server.config.{config_name.capitalize()}Config"

    app.config.from_object(config_object)

    @app.route("/api/v1")
    def root_api():
        return jsonify({"Hello": "World!"})

    @app.route("/api/v1/member", methods = ["GET", "POST"])
    def member_api():
        return jsonify({'member': "api"})

    return app
