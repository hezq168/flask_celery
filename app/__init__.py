# -*- coding:utf-8 -*-
__author__ = 'Administrator'
# -*- coding:utf-8 -*-
from flask import Flask
from config import Config
from celery import Celery, platforms

config = Config()
celery = Celery(__name__, broker=config.CELERY_BROKER_URL)

# 程序初始化
def create_app():
    app = Flask(__name__)
    app.config.from_object(config)
    config.init_app(app)

    # 初始化celery
    celery.conf.update(app.config)
    TaskBase = celery.Task
    class ContextTask(TaskBase):
        abstract = True
        def __call__(self, *args, **kwargs):
            with app.app_context():
                return TaskBase.__call__(self, *args, **kwargs)
    celery.Task = ContextTask
    # linux下root启动celery
    #platforms.C_FORCE_ROOT = True


    return app