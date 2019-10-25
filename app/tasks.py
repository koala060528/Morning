import requests, json
from apscheduler.schedulers.background import BackgroundScheduler
from config import Config
from app import redis


def get_access_token():
    url = 'https://api.weixin.qq.com/cgi-bin/token?grant_type=client_credential&appid=%s&secret=%s' % (
        Config.APPID, Config.APPSECRET)
    js = json.loads(requests.get(url=url).text)
    if js.get('access_token'):
        # 在Redis中存贮access_token，过期时间设置为7200s
        redis.set('access_token', js.get('access_token'), ex=7200)
        print('get access_token success')


def schedule(interval=7200):  # 默认间隔设置为7200秒
    get_access_token()
    scheduler = BackgroundScheduler()
    scheduler.add_job(get_access_token, 'interval', seconds=interval)
    scheduler.start()
