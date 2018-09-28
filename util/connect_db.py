#coding:utf-8
import pymysql.cursors
import json
class OperationMysql:
	def __init__(self):
		self.conn = pymysql.connect(
			host='10.10.13.71',
			port=3306,
			user='root',
			passwd='root-jc-211@#$',
			db='jc_oa',
			charset='utf8',
			cursorclass=pymysql.cursors.DictCursor
			)
		self.cur = self.conn.cursor()

	#查询一条数据
	def search_one(self,sql):
		self.cur.execute(sql)
		# result = self.cur.fetchall()
		result = self.cur.fetchone()
		result = json.dumps(result, ensure_ascii=False)
		return result

	#查询多条数据
	def search_all(self,sql):
		self.cur.execute(sql)
		result = self.cur.fetchall()
		# result = self.cur.fetchone()
		result = json.dumps(result, ensure_ascii=False)
		return result


if __name__ == '__main__':
	op_mysql = OperationMysql()
	res = op_mysql.search_all("select * from oa_obs where status = 1 and isno_company = 1")
	print(res)