from flask import Flask
from config import Config
from redis import Redis

app = Flask(__name__)
app.config.from_object(Config)


from app import auth, tasks

tasks.schedule()
