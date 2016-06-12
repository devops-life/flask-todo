#!/usr/bin/env python
# encoding: utf-8


"""
@author: chenzhangpeng
@contact: chen_zhangpeng@163.com
@site: http://www.qinqinbaby.com
@file: models.py
@time: 16/6/8 下午2:25
"""

from app import db
import datetime
from flask_mongoengine.wtf import model_form

class Todo(db.Document):
    content = db.StringField(required=True,max_length=20)
    time = db.DateTimeField(default=datetime.datetime.now())
    status = db.IntField(default=0)

TodoForm = model_form(Todo)