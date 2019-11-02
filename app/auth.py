from app import app
from flask import request
import hashlib
from config import Config
import os
from datetime import datetime
from app.tasks import post
import json
import xml.etree.ElementTree as ET


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
        xml_rec = ET.fromstring(rec)
        toUser = xml_rec.find('ToUserName').text
        fromUser = xml_rec.find('FromUserName').text
        messageType = xml_rec.find('MsgType').text
        content = xml_rec.find('Content').text
        with open(file_path, 'a+', encoding='utf-8') as f:
            f.writelines(str(datetime.now()))
            f.writelines('\n')
            f.writelines(rec.decode())
            f.writelines('\n')
            f.writelines('\n')

        xml_ret = '<xml><ToUserName><![CDATA[%s]]></ToUserName><FromUserName><![CDATA[' \
                  '%s]]></FromUserName><CreateTime>%s</CreateTime><MsgType><![CDATA[text]]></MsgType><Content><![' \
                  'CDATA[%s]]></Content></xml> '
        if fromUser == Config.MY_OPENID and content == '早安':
            res = post()
            if res:
                content = '成功'
            else:
                content = '失败'
        xml_ret = xml_ret % (fromUser, toUser, datetime.now(), content)
        return xml_ret


@app.route('/test', methods=['GET'])
def test():
    return str(datetime.now())
