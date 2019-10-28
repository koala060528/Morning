import os
from dotenv import load_dotenv

basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(basedir, '.env'))


class Config(object):
    # 公众号设置
    TOKEN = os.environ.get('TOKEN')
    APPID = os.environ.get('APPID')
    APPSECRET = os.environ.get('APPSECRET')
    HER_OPENID = os.environ.get('HER_OPENID')
    MY_OPENID = os.environ.get('MY_OPENID')
    TEMPLATE = os.environ.get('MESSAGE_TEMPLATE')
    POST_URL = url = 'https://api.weixin.qq.com/cgi-bin/message/template/send?access_token={0}'

    # redis设置
    REDIS_URL = os.environ.get('REDIS_URL')

    # 模板ID
    MESSAGE_TEMPLATE = os.environ.get('MESSAGE_TEMPLATE')

    # 配置
    HER_LOCATION = os.environ.get('HER_LOCATION')
    MY_LOCATION = os.environ.get('MY_LOCATION')
    ANNIVERSARY = os.environ.get('ANNIVERSARY')
    EXPECTED_DAY = os.environ.get('EXPECTED_DAY')

    # 天气服务
    HEWEATHER_KEY = os.environ.get('HEWEATHER_KEY')
    WEATHER_URL = 'https://free-api.heweather.net/s6/{0}/{1}?{2}&key=' + HEWEATHER_KEY

    # 每日一言
    DAILY_YY = 'https://api.lovelive.tools/api/SweetNothings'
