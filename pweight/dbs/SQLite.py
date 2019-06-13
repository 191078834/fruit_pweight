#!/usr/bin/python
# -*- coding: utf-8 -*-
import sqlite3
import sys


class Singleton(object):
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, 'con'):
            cls._inst = super(Singleton, cls).__new__(cls, *args, **kwargs)
        return cls._inst


class Sqlpite_db(Singleton):
    def __init__(self):
        super(Sqlpite_db, self).__init__()

        if not hasattr(self, 'con'):
            try:
                self.conn = sqlite3.connect('./test.db')
                self.st = self.conn.cursor()
            except Exception as e:
                raise
            else:
                pass
                #log.debug('连接到数据库 %s' % db)
    # 自创建表表

    def create_table(self):
        self.st.execute('''CREATE TABLE fruits_info
               (
                fruits  text  PRIMARY KEY                 NOT NULL
               );''')
        # purchase_shop_info
        # create_time text     NOT NULL,
        # path       text     NOT NULL

    def drop_table(self, sql):
        try:
            self.st.execute(sql)
        except Exception as e:
            raise

    def add(self, sql):
        try:
            self.st.execute(sql)
            self.conn.commit()
            print "ok"
        except Exception as e:
            pass

    def select(self, sql):
        try:
            INFO = self.st.execute(sql)
        except Exception as e:
            raise
        return INFO.fetchall()

    def delete(self, sql):
        try:
            self.st.execute(sql)
            self.conn.commit()
        except Exception as e:
            raise

    def update(self, sql):
        try:
            self.st.execute(sql)
            self.conn.commit()
        except Exception as e:
            raise
# s = Sqlpite_db()
# s.create_table()
#
# # s.drop_table(sql)
# s.create_table()
# sql = "insert into purchase_shop_info(ID, TIME, TIMESTAMP) values ('[\'233445\']', '2018-10-21 19:23:32', '12121345')"
# s.add(sql=sql)
# sql2 = "SELECT ID, TIME, TIMESTAMP from purchase_shop_info"
# cons = s.select(sql2)
# for i in cons:
#     print i[0], i[1],i[2]
