#coding=utf-8

from flask import Flask
from flask import Blueprint
from flask import jsonify
import littlebeanfund as lbf

app = Flask(__name__)
api = Blueprint('api', __name__)


@api.route('/funds/', methods=['GET'])
def get_funds():
    # funds_list = [
    #     ("000831", "工银医疗保健"),
    #     ("001076", "易方达改革红利"),
    #     ("001272", "兴业聚利灵活")
    # ]
    return jsonify(lbf.get_funds())


@api.route('/funds/top10/', methods=['GET'])
def get_top10():
    return jsonify(lbf.get_top10())


@api.route('/funds/top10/<fund_type>', methods=['GET'])
def get_top10_by_type(fund_type):
    return jsonify(lbf.get_top10_by_type(fund_type))


if __name__ == '__main__':
    app.config['JSON_AS_ASCII'] = False
    app.config['JSONIFY_MIMETYPE'] = 'application/json; charset=utf-8'
    app.register_blueprint(api, url_prefix="/api")
    app.run(debug=True)
