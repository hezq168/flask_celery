# -*- coding:utf-8 -*-
__author__ = 'Administrator'
from celery.schedules import timedelta
from celery.schedules import crontab


class Config:
    DEBUG = True
#   celery配置
    CELERY_BROKER_URL = 'redis://localhost:6379/2'
    CELERY_RESULT_BACKEND = 'redis://localhost:6379/3'
    CELERY_ALWAYS_EAGER = True
#   注册任务
    CELERY_IMPORTS = ("app.tasks",)
#   数据获取、分析周期设置
    CELERYBEAT_SCHEDULE = {
        'job1': {
          'task': 'app.tasks.tk.job1',
          'schedule': crontab(minute=00, hour=11),
          'args': (),
        },
        'job2': {
            'task': 'app.tasks.job2',
            'schedule': timedelta(seconds=10),
            'args': (),
        },
    }
#   celery时区
    CELERY_TIMEZONE = 'Asia/Shanghai'


    @staticmethod
    def init_app(app):
        pass
