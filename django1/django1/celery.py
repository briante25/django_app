# celery.py
from __future__ import absolute_import, unicode_literals
import os
from celery import Celery

# 設置 Django 的環境變量
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django1.settings')

# 創建一個 Celery 實例
app = Celery('django1')

# 使用 Django 配置文件設置 Celery
app.config_from_object('django.conf:settings', namespace='CELERY')

# 自動從所有已註冊的 Django app 中加載任務模塊
app.autodiscover_tasks()
