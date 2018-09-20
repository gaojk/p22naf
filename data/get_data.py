#coding:utf-8
from util.operation_excel import OperationExcel
from data import data_config
from util.operation_json import OperetionJson
from util.connect_db import OperationMysql
class GetData:
	def __init__(self, path, sheetNum):
		self.opera_excel = OperationExcel(path, sheetNum)
		# self.opera_excel = OperationExcel('../dataconfig/OA.xls', 0)

	#去获取excel行数,就是我们的case个数
	def get_excel_name(self):
		return self.opera_excel.get_name()


	#去获取excel行数,就是我们的case个数	
	def get_case_lines(self):
		return self.opera_excel.get_lines()

	#获取是否执行
	def get_is_run(self,row):
		flag = None
		col = int(data_config.get_run())
		run_model = self.opera_excel.get_cell_value(row,col)
		if run_model == 'yes':
			flag = True
		else:
			flag = False
		return flag

	#是否携带header
	def is_header(self,row):
		col = int(data_config.get_header())
		header = self.opera_excel.get_cell_value(row,col)
		if header != '':
			return header
		else:
			return None

	#获取请求方式
	def get_request_method(self,row):
		col = int(data_config.get_run_way())
		request_method = self.opera_excel.get_cell_value(row,col)
		return request_method

	#获取case id
	def get_case_id(self,row):
		col = int(data_config.get_id())
		id = self.opera_excel.get_cell_value(row,col)
		return id

	#获取case名称
	def get_case_name(self,row):
		col = int(data_config.get_name())
		id = self.opera_excel.get_cell_value(row,col)
		return id

	#获取url
	def get_request_url(self,row):
		col = int(data_config.get_url())
		url = self.opera_excel.get_cell_value(row,col)
		return url

	#获取请求数据
	def get_request_data(self,row):
		col = int(data_config.get_data())
		data = self.opera_excel.get_cell_value(row,col)
		if data == '':
			return None
		return data

	#通过获取关键字拿到data数据
	def get_data_for_json(self,row):
		# 通过json_path单元格获取制定的json模块的data(excel的json路径列)
		json_path = self.get_path_json(row)
		opera_json = OperetionJson(json_path)
		request_data = opera_json.get_data(self.get_request_data(row))
		return request_data

	#获取预期结果
	def get_expcet_data(self,row):
		col = int(data_config.get_expect())
		# print "预期结果"
		expect = self.opera_excel.get_cell_value(row,col)
		if expect == '':
			return None
		return expect

	#获取用来做结果比对的sql查询语句
	def get_sql_result_data(self,row):
		col = int(data_config.get_sql_result())
		# print "获取用来做结果比对的sql查询语句"
		sql_result = self.opera_excel.get_cell_value(row,col)
		if sql_result == '':
			return None
		return sql_result

	#获取sql依赖单元格的查询语句
	def get_sql_rely_result_data(self,row):
		col = int(data_config.get_data_depend_sql())
		# print "获取sql依赖单元格的查询语句"
		sql_result = self.opera_excel.get_cell_value(row,col)
		if sql_result == '':
			return None
		return sql_result

	#通过sql获取预期结果
	def get_one_sql_data(self, row, get_data):
		sql = get_data(row)
		# print sql
		# 这里做判断，预期结果内有sql命令，才去运行sql
		if sql != None:
			op_mysql = OperationMysql()
			res = op_mysql.search_one(sql)
			# return res.decode('unicode-escape')
			# print(res.encode('utf-8').decode('gb18030'))
			# print(type((res.encode('utf-8').decode('gb18030'))))
			return res.encode('utf-8').decode('unicode_escape')

		else:
			return None

	def get_all_sql_data(self,row, get_data):
		sql = get_data(row)
		# print sql
		# 这里做判断，预期结果内有sql命令，才去运行sql
		if sql != None:
			op_mysql = OperationMysql()
			res = op_mysql.search_all(sql)
			# return res.decode('unicode-escape')
			# print(res.encode('utf-8').decode('gb18030'))
			# print(type((res.encode('utf-8').decode('gb18030'))))
			return res.encode('utf-8').decode('unicode_escape')
		else:
			return None


	#写响应结果到实际结果列
	def write_result(self,row,value):
		col = int(data_config.get_responde_result())
		self.opera_excel.write_value(row,col,value)

	#写测试结果到测试结果列
	def write_result_status(self,row,value):
		col = int(data_config.get_result_status())
		self.opera_excel.write_value(row,col,value)

	#写响应结果返回值到返回状态列
	def write_code_responde_result(self,row,value):
		col = int(data_config.get_code_responde_result())
		self.opera_excel.write_value(row,col,value)

	#写请求数据内容到请求数据内容列
	def write_request_data_result(self,row,value):
		col = int(data_config.get_request_data_result())
		self.opera_excel.write_value(row,col,value)

	#写数据库查询结果到sql查询结果
	def write_sql_result(self,row,value):
		col = int(data_config.write_sql_result())
		self.opera_excel.write_value(row,col,value)

	#将sql查询出、返回状态、实际结果、请求数据内容和测试结果列的结果置空
	def write_void_to_output_cell(self,row,value):
		col = int(data_config.write_sql_result())
		self.opera_excel.write_value(row,col,value)
		col = int(data_config.get_code_responde_result())
		self.opera_excel.write_value(row, col, value)
		col = int(data_config.get_responde_result())
		self.opera_excel.write_value(row, col, value)
		col = int(data_config.get_request_data_result())
		self.opera_excel.write_value(row, col, value)
		col = int(data_config.get_result_status())
		self.opera_excel.write_value(row, col, value)

	#获取依赖数据的key
	def get_depend_key(self,row):
		col = int(data_config.get_data_depend())
		depent_key = self.opera_excel.get_cell_value(row,col)
		if depent_key == "":
			return None
		else:
			return depent_key

	#判断是否有case依赖
	def is_depend(self,row):
		col = int(data_config.get_case_depend())
		depend_case_id = self.opera_excel.get_cell_value(row,col)
		if depend_case_id == "":
			return None
		else:
			return depend_case_id

	#判断是否有sql查询case的依赖
	def is_depend_sql(self,row):
		col = int(data_config.get_data_depend_sql())
		depend_sql = self.opera_excel.get_cell_value(row,col)
		# print "depend_sql"
		# print depend_sql

		if depend_sql == "":
			return None
		else:
			return depend_sql

	#获取数据依赖字段
	def get_depend_field(self,row):
		col = int(data_config.get_field_depend())
		data = self.opera_excel.get_cell_value(row,col)
		if data == "":
			return None
		else:
			return data

	#获取对应测试模块josn文件的路径
	def get_path_json(self,row):
		col = int(data_config.get_json_path())
		json_path = self.opera_excel.get_cell_value(row,col)
		return json_path

class GetExcelDataOfJson:
	def __init__(self):
		pass

	def get_json_of_excel(self):
		#通过jsonOfExcel.json文件获取要执行的excel名字，如果在字典中该key对应的value是yes的话，就读取这个excel
		self.get_json_of_excel = OperetionJson('../dataconfig/jsonOfExcel.json')
		getJsonOfExcel = self.get_json_of_excel.read_data()
		return getJsonOfExcel

if __name__ == '__main__':
	run = GetData('../dataconfig/OA.xls', 0)
	print(run.get_excel_name())
	print(run.get_one_sql_data(44, run.get_sql_rely_result_data))
	# print run.is_depend_sql(1)
	# op_json = run.get_data_for_json(5)
	# print type(op_json)
	# print op_json

