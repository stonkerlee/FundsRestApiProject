#coding=utf-8

from flask import Flask
from flask import Blueprint
from flask import jsonify

app = Flask(__name__)
api = Blueprint('api', __name__)

@api.route('/funds/', methods=['GET'])
def get_funds():
    json_list = {
        "000831" : "工银医疗保健",
        "001076" : "易方达改革红利",
        "001272" : "兴业聚利灵活"
    }
    return jsonify(json_list)

if __name__ == '__main__':
    app.config['JSON_AS_ASCII'] = False
    app.register_blueprint(api, url_prefix="/api")
    app.run(debug=True)
