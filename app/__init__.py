from flask import Flask
from config import Config
from redis import Redis

app = Flask(__name__)
app.config.from_object(Config)

redis = Redis.from_url(Config.REDIS_URL)

from app import auth, tasks

tasks.schedule(7200)
