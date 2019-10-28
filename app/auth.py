from app import app
from flask import request
import hashlib
from config import Config
import os
from datetime import datetime


@app.route('/handle', methods=['GET', 'POST'])
def auth():
    if request.method == 'GET':
        signature = request.args.get('signature')
        timestamp = request.args.get('timestamp')
        nonce = request.args.get('nonce')
        echostr = request.args.get('echostr')
        token = Config.TOKEN

        list = [token, timestamp, nonce]
        list.sort()

        temp = ''.join(list)

        sha1 = hashlib.sha1()
        sha1.update(temp.encode('utf-8'))
        hashcode = sha1.hexdigest()

        if hashcode == signature:
            return echostr
        else:
            return ""
    elif request.method == 'POST':
        print('post request')
        rec = request.stream.read()
        path = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'log')
        if not os.path.exists(path):
            os.mkdir(path)
        file_path = os.path.join(path, 'requestRecord.txt')
        with open(file_path, 'wb') as f:
            f.write(str(datetime.now()).encode())
            f.write(rec)
