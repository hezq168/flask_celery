# -*- coding:utf-8 -*-
__author__ = 'Administrator'
from app import celery



@celery.task()
def job1():
    return 'job1'

@celery.task()
def job2():
    return 'job2'