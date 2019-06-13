#!/usr/bin/python
# -*- coding: utf-8 -*-
from datetime import datetime
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy import create_engine
from model import Device, Task, Fruit, Order

import threading
import model

DEFAUL_DATABASE_PATH = 'pweight.db'

DEVICE_STATUS = ["installing", "running", "stopping", 'continue_weight', 'idle']
TASK_STATUS = ["waiting_weight", "taking_photo", "identifying", "waiting_select",
               "confirning", "paying", "unidentified", "payment_timeout", "confirm_timeout",
               "select_timeout", "payed", "canceled", "network_disconnection"]
ORDER_STATUS = {"generating", "waiting", "canceled", "finished", "timeout", "network_disconnection"}
PAY_WAY = ["ali", "wechat"]


engine = create_engine('sqlite:////home/pweight/pweight/dbs/pweight.sqlite')
session_factory = sessionmaker(bind=engine)
Session = scoped_session(session_factory)


class DBApi(object):
    _instance_lock = threading.Lock()

    def __new__(cls, *args, **kwargs):
        if not hasattr(DBApi, "_instance"):
            with DBApi._instance_lock:
                if not hasattr(DBApi, "_instance"):
                    DBApi._instance = object.__new__(cls)
        return DBApi._instance

    def __init__(self, database_path=DEFAUL_DATABASE_PATH):
        self.db_file = database_path

    @staticmethod
    def get_session():
        return Session()

    def create_tables(self, device_id):
        engine = create_engine('sqlite:///%s' % self.db_file)
        # 创建表结构
        model.Base.metadata.create_all(engine)
        session = self.get_session()
        device = session.query(Device).first()
        if device is None:
            device = Device(id=device_id, status='idle')
        else:
            device.id = device_id
            device.status = 'idle'
        session.add(device)
        session.commit()
        session.close()

    def model_query(self, *args, **kwargs):
        session = self.get_session()
        query = session.query(*args)
        return query

    def get_device_id(self):
        session = self.get_session()
        device_id = session.query(Device).first().id
        session.close()
        return device_id

    def get_device_req_id(self):
        session = self.get_session()
        req_id = session.query(Device).first().reqId
        session.close()
        return req_id

    def update_device_req_id(self, new_req_id):
        session = self.get_session()
        device = session.query(Device).first()
        device.reqId = new_req_id
        session = self.get_session()
        session.add(device)
        session.commit()
        session.close()

    def get_device_task_id(self):
        session = self.get_session()
        task_id = session.query(Device).first().taskId
        session.close()
        return task_id

    def update_device_task_id(self, new_task_id):
        session = self.get_session()
        device = session.query(Device).first()
        device.taskId = new_task_id
        session = self.get_session()
        session.add(device)
        session.commit()
        session.close()

    def get_device_status(self):
        session = self.get_session()
        status = session.query(Device).first().status
        session.close()
        return status

    def update_device_status(self, new_status):
        session = self.get_session()
        device = session.query(Device).first()
        device.status = new_status
        session = self.get_session()
        session.add(device)
        session.commit()
        session.close()

    def insert_task(self, task_dict):
        task = Task(id=task_dict.get('id'),
                    createTime=datetime.now(),
                    updateTime=None,
                    reqId=task_dict.get('reqId'),
                    status=task_dict.get('status'),
                    photoPath=task_dict.get('photoPath'),
                    recordId=task_dict.get('recordId'),
                    identified_code=task_dict.get('code'),
                    identified_msg=task_dict.get('msg'))
        session = self.get_session()
        session.add(task)
        session.commit()
        session.close()

    def get_tasks_by_req_id(self, req_id):
        session = self.get_session()
        tasks = session.query(Task).filter_by(reqId=req_id).all()
        session.close()
        return tasks

    def update_task_status(self, task_id, new_status):
        if new_status in TASK_STATUS:
            session = self.get_session()
            task = session.query(Task).filter_by(id=task_id).first()
            task.status = new_status
            task.updateTime = datetime.now()
            session = self.get_session()
            session.add(task)
            session.commit()
            session.close()

    def update_task_weight(self, task_id, weight):
        session = self.get_session()
        task = session.query(Task).filter_by(id=task_id).one()
        task.weight = weight
        task.updateTime = datetime.now()
        session = self.get_session()
        session.add(task)
        session.commit()
        session.close()

    def update_task_identified_info(self, task_id, record_id, identified_code, identified_msg, weight):
        session = self.get_session()
        task = session.query(Task).filter_by(id=task_id).one()
        task.updateTime = datetime.now()
        task.recordId = record_id
        task.identified_code = identified_code
        task.identified_msg = identified_msg
        task.weight = weight
        session = self.get_session()
        session.add(task)
        session.commit()
        session.close()

    def insert_fruit(self, fruit_dict):
        fruit = Fruit(id=fruit_dict.get('id'),
                      reqId=fruit_dict.get('reqId'),
                      taskId=fruit_dict.get('taskId'),
                      recordId=fruit_dict.get('recordId'),
                      createTime=datetime.now(),
                      updateTime=None,
                      selected=fruit_dict.get('selected', False),
                      confirmed=fruit_dict.get('confirmed', False),
                      goodsId=fruit_dict.get('goodsId'),
                      goodsName=fruit_dict.get('goodsName'),
                      goodsNo=fruit_dict.get('goodsNo'),
                      price=fruit_dict.get('price'),
                      calculateType=fruit_dict.get('calculateType'),
                      goodsPrice=fruit_dict.get('goodsPrice'),
                      priceUnit=fruit_dict.get('priceUnit'),
                      weight=fruit_dict.get('weight'),
                      num=fruit_dict.get('num'),
                      total=fruit_dict.get('total'),
                      discount=fruit_dict.get('discount'),
                      fact=fruit_dict.get('fact'),
                      imgUrl=fruit_dict.get('imgUrl'))
        session = self.get_session()
        session.add(fruit)
        session.commit()
        session.close()

    def update_fruit_info(self, fruit):
        session = self.get_session()
        session.add(fruit)
        session.commit()
        session.close()

    def get_fruits_by_req_id(self, req_id):
        task_ids = self.get_tasks_by_req_id(req_id)
        fruits = []
        for taskId in task_ids:
            fruits.append(self.get_fruits_by_task_id(taskId))
        return fruits

    def get_selected_fruits_by_req_id(self, req_id):
        result = []
        session = self.get_session()
        result = session.query(Fruit).filter_by(reqId=req_id, selected=True).all()
        session.close()
        return result

    def get_confirmed_fruits_by_req_id(self, req_id):
        result = []
        session = self.get_session()
        result = session.query(Fruit).filter_by(reqId=req_id, confirmed=True).all()
        session.close()
        return result

    def get_fruits_by_task_id(self, task_id):
        result = []
        session = self.get_session()
        result = session.query(Fruit).filter_by(taskId=task_id).all()
        session.close()
        return result

    def get_fruits_by_record_id(self, record_id):
        result = []
        session = self.get_session()
        result = session.query(Fruit).filter_by(recordId=record_id).all()
        session.close()
        return result

    def get_fruits_by_order_id(self, *args, **kwargs):
        pass

    def confirm_fruit(self, fruit_id, fruit_dict):
        session = self.get_session()
        fruit = session.query(Fruit).filter_by(id=fruit_id).one()
        fruit.updateTime = datetime.now()
        for key, value in fruit_dict.items():
            fruit.__setattr__(key, value)

        fruit.confirmed = True
        session = self.get_session()
        session.add(fruit)
        session.commit()
        session.close()

    def select_fruit(self, index_id):
        session = self.get_session()
        fruit = session.query(Fruit).filter_by(id=index_id).first()
        fruit.selected = True
        fruit.updateTime = datetime.now()
        session = self.get_session()
        session.add(fruit)
        session.commit()
        session.close()

    def not_select_fruit(self, index_id):
        session = self.get_session()
        fruit = session.query(Fruit).filter_by(id=index_id).first()
        fruit.selected = True
        fruit.updateTime = datetime.now()
        session = self.get_session()
        session.add(fruit)
        session.commit()
        session.close()

    def insert_order(self, order_dict):
        order = Order(id=order_dict.get('id'),
                      reqId=order_dict.get('reqId'),
                      createTime=datetime.now(),
                      updateTime=None,
                      status=order_dict.get('status'),
                      total=order_dict.get('total'),
                      payWay=order_dict.get('pay_way'))
        session = self.get_session()
        session.add(order)
        session.commit()
        session.close()

    def get_order_by_req_id(self, req_id):
        session = self.get_session()
        order = session.query(Order).filter_by(reqId=req_id).first()
        session.close()
        return order

    def get_order_status(self, order_id):
        session = self.get_session()
        status = session.query(Order).filter_by(id=order_id).first().status
        session.close()
        return status

    def update_order_status(self, order_id, new_status):
        if new_status in ORDER_STATUS:
            session = self.get_session()
            order = session.query(Order).filter_by(id=order_id).first()
            order.status = new_status
            order.updateTime = datetime.now()
            session = self.get_session()
            session.add(order)
            session.commit()
            session.close()

