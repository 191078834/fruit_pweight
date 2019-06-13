#!/usr/bin/python
# -*- coding: utf-8 -*-

from sqlalchemy import Column, String, Boolean, Integer, ForeignKey, DateTime
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base


# 创建对象的基类:
Base = declarative_base()


# 定义User对象:
class Device(Base):
    # 表的名字:
    __tablename__ = 'device'

    # 表的结构:
    id = Column(String(36), primary_key=True)
    reqId = Column(String(36))
    taskId = Column(String(36))
    status = Column(String(15))


class Task(Base):
    # 表的名字:
    __tablename__ = 'tasks'

    # 表的结构:
    id = Column(String(36), primary_key=True)
    createTime = Column(DateTime)
    updateTime = Column(DateTime, nullable=True)
    reqId = Column(String(36))
    status = Column(String(15))
    photoPath = Column(String(100), nullable=True)
    weight = Column(Integer, nullable=True)
    recordId = Column(String(32), nullable=True)
    identified_code = Column(Integer, nullable=True)
    identified_msg = Column(String(200), nullable=True)


class Fruit(Base):

    # 表的名字:
    __tablename__ = 'fruits'

    # 表的结构:
    id = Column(String(36), primary_key=True)
    reqId = Column(String(36))
    taskId = Column(String(36))
    recordId = Column(String(36), nullable=True)
    createTime = Column(DateTime)
    updateTime = Column(DateTime, nullable=True)
    selected = Column(Boolean, nullable=True, default=False)
    confirmed = Column(Boolean, nullable=True, default=False)
    goodsId = Column(String(36), nullable=True)
    goodsName = Column(String(36), nullable=True)
    goodsNo = Column(String(36), nullable=True)
    price = Column(String(36), nullable=True)
    calculateType = Column(Integer, nullable=True)
    goodsPrice = Column(Integer, nullable=True)
    priceUnit = Column(Integer, nullable=True)
    weight = Column(Integer, nullable=True)
    num = Column(Integer, nullable=True)
    total = Column(Integer, nullable=True)
    discount = Column(Integer, nullable=True)
    fact = Column(Integer, nullable=True)
    imgUrl = Column(String(200), nullable=True)
    PhotoPath = Column(String(200), nullable=True)



class Order(Base):
    
    # 表的名字:
    __tablename__ = 'orders'

    # 表的结构:
    id = Column(String(36), primary_key=True)
    reqId = Column(String(36))
    createTime = Column(DateTime)
    updateTime = Column(DateTime, nullable=True)
    status = Column(String(20))
    total = Column(Integer)
    payWay = Column(String(10))


# 初始化数据库连接:
# engine = create_engine('sqlite:///pweight.db')

# 创建表结构
# Base.metadata.create_all(engine)

# 创建DBSession类型:
# DBSession = sessionmaker(bind=engine)

# session = DBSession()
# device = Device(id="123456", reqId="2d54f60c56a8475fa97e3c1874097f10", taskId="2d54f60c56a8475fa97e3c1874097f10", status='running')
# session.add(device)
# session.commit()
# session.close()


