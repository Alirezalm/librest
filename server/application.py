import json

from flask import Flask, jsonify, request

from src.controllers import MemberInsertController


def create_server(config_name: str):
    app = Flask(__name__)

    config_object = f"server.config.{config_name.capitalize()}Config"

    app.config.from_object(config_object)

    @app.route("/api/v1")
    def root_api():
        return jsonify({"Hello": "World!"})

    @app.route("/api/v1/member", methods = ["GET", "POST"])
    def member_api():
        member_data = json.loads(request.data)
        MemberInsertController(member_data)
        return jsonify({'member': "api"})

    return app
