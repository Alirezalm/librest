import json

from flask import Flask, jsonify, request

from src.controllers import MemberInsertController, MemberListController


def create_server(config_name: str):
    app = Flask(__name__)

    config_object = f"server.config.{config_name.capitalize()}Config"

    app.config.from_object(config_object)

    @app.route("/api/v1")
    def root_api():
        return jsonify({"Hello": "World!"})

    @app.route("/api/v1/member", methods = ["GET", "POST"])
    def member_api():
        if request.method == 'POST':
            member_data = json.loads(request.data)
            MemberInsertController(member_data)
            return jsonify({'status': "inserted"})
        else:
            member_list_controller = MemberListController()
            data_to_serialize = member_list_controller.make_data()

            return jsonify(data_to_serialize)
    return app
