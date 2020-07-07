#! /usr/bin/python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 29 13:33:20 2019

written by pyleo
"""

import settings
from flask import Flask, request, jsonify, send_from_directory
import os

app = Flask(__name__)


@app.route("/check_version/", methods=['POST'])
def check_version():
    """检查版本
    
    :return: None
    """
    if not request.get_data():
        return jsonify(success=False)
    else:
        try:
            return_json = {"success": True, "version": settings.VERSION, "edition": settings.EDITION,
                           "update_version": False, "update_edition": False, "update_files": []}
            get_json = eval(request.get_data())
            version = get_json['version']
            edition = get_json['edition']
            local_version = settings.VERSION
            local_edition = settings.EDITION
            if int(version.replace(".", "")) < int(local_version.replace(".", "")):        # 比对大版本
                return_json['update_version'] = True
            if int(edition.replace(".", "")) < int(local_edition.replace(".", "")):        # 比对小版本
                return_json['update_edition'] = True
            return_json['update_files'] = settings.UPDATE_FILES
        except Exception as ex:
            return jsonify(success=False)
        else:
            return jsonify(return_json)


@app.route("/download/settings.pyd", methods=['GET'])
def download_config():
    directory = os.getcwd()  # 当前目录
    return send_from_directory(directory, "source_file/settings.pyd", as_attachment=True)


@app.route("/download/login.pyd", methods=['GET'])
def download_login():
    directory = os.getcwd()
    return send_from_directory(directory, "source_file/login.pyd", as_attachment=True)


@app.route("/download/order.pyd", methods=['GET'])
def download_order():
    directory = os.getcwd()
    return send_from_directory(directory, "source_file/order.pyd", as_attachment=True)


@app.route("/download/scramble.pyd", methods=['GET'])
def download_scramble():
    directory = os.getcwd()
    return send_from_directory(directory, "source_file/scramble.pyd", as_attachment=True)


@app.route("/download/browser.pyd", methods=['GET'])
def download_browser():
    directory = os.getcwd()
    return send_from_directory(directory, "source_file/browser.pyd", as_attachment=True)


if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=8888)
