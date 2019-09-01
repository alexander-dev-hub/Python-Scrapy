# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import json
import codecs

import pymysql

class ScrapyMysqlPipeline(object):
    def getConnection(self):
        config = {
            'host': '127.0.0.1',
            'port': 3306,
            'user': 'root',
            'password': '',
            'database': 'wx',
            'charset': 'utf8',
            'cursorclass': pymysql.cursors.DictCursor
        }
        connection = pymysql.connect(**config)
        return connection

    # pipeline默认调用
    def process_item(self, item, spider):
        connection = self.getConnection()
        try:
            with connection.cursor() as cursor:
                # 执行sql语句，插入记录
                sql = "insert into spider_test(name,url,icon,date) values(%s,%s,%s,%s)"
                params = (item["name"], item["url"], item["icon"], item["date"])
                cursor.execute(sql, params);
                # 没有设置默认自动提交，需要主动提交，以保存所执行的语句
                connection.commit()
        finally:
            connection.close()


class ScrapyJsonPipeline(object):
	def __init__(self):
		self.file = codecs.open('result.json', 'w', encoding='utf-8') #크롤링 데이터를 저장할 파일 OPEN
		
	def process_item(self, item, spider):
		line = json.dumps(dict(item), ensure_ascii=False) + "\n" #Item을 한줄씩 구성
		self.file.write(line) #파일에 기록
		return item
		
	def spider_closed(self, spider):
		self.file.close()	#파일 CLOSE