import os
from dotenv import load_dotenv

basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(basedir, '.env'))


class Config(object):
    # 公众号设置
    TOKEN = os.environ.get('TOKEN')
    APPID = os.environ.get('APPID')
    APPSECRET = os.environ.get('APPSECRET')

    # redis设置
    REDIS_URL = os.environ.get('REDIS_URL')

    # 模板ID
    MESSAGE_TEMPLATE = os.environ.get('MESSAGE_TEMPLATE')
