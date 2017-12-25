# flask_celery

介绍如何使用celery + flask 在项目中

安装 celery==3.1.17 redis
使用方法

windows想使用celery 需要开2个命令窗口,在(vir))下

1、celery -A celery_worker.celery  worker -l info


2、celery beat -A celery_worker.celery -l info

liunx

celery work -B -A celery_worker.celery -l info