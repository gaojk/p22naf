#coding:utf-8
import sys, json
sys.path.append("../")
from base.runmethod import RunMethod
from data.get_data import GetData
from data.get_data import GetExcelDataOfJson
from util.common_util import CommonUtil
from data.dependent_data import DependdentData
from util.send_email import SendEmail
from util.operation_header import OperationHeader
from util.operation_json import OperetionJson

class RunTest:
	def __init__(self):
		self.run_method = RunMethod()
		self.data_json_of_excel = GetExcelDataOfJson()
		self.com_util = CommonUtil()
		self.send_mai = SendEmail()

	#程序执行的
	def go_on_run(self):
		#通过data_json_of_excel来获取json文件里面保存的excel文件名，然后根据字典里面的value值是否为yes来确定执行相应的excel
		get_json_of_excel = self.data_json_of_excel.get_json_of_excel()
		#这里的for循环是为了控制遍历执行json文件中的所有需执行的excel文件
		for jsonOfExcelDict in get_json_of_excel:
			if get_json_of_excel[jsonOfExcelDict].lower() == 'yes':
				excel_path = '../dataconfig/' + jsonOfExcelDict + '.xls'
				self.data = GetData(excel_path, 0)
			else:
				continue
			res = None
			pass_count = []
			fail_count = []
			#10  0,1,2,3
			rows_count = self.data.get_case_lines()
			#置空上次接口测试的结果
			# for i in range(1, rows_count):
			# 	self.data.write_void_to_output_cell(i, " ")
			# 	print(self.data.get_case_name(i))
			#开始接口测试
			for i in range(1,rows_count):
				is_run = self.data.get_is_run(i)
				if is_run:
					case_id = self.data.get_case_id(i)
					case_name = self.data.get_case_name(i)
					# 显示当前正在执行的case的id和name，用来在报错的时候定位是那一条case出问题了
					print(case_id + "---" + case_name)
					url = self.data.get_request_url(i)
					method = self.data.get_request_method(i)
					request_data = self.data.get_data_for_json(i)
					#这是mss老师当时把预期结果里面的sql语111句查询出来，然后返回到expect里面的写法
					# expect = self.data.get_one_sql_data(i, self.data.get_expcet_data)
					expect = self.data.get_expcet_data(i)
					# RunTestPrint
					# print(expect)
					# print(type(expect))
					header = self.data.is_header(i)
					depend_case = self.data.is_depend(i)
					depend_case_sql = self.data.is_depend_sql(i)
					if depend_case != None:
						self.depend_data = DependdentData(depend_case, excel_path, 0)
						#获取的依赖响应数据
						depend_response_data = self.depend_data.get_data_for_key(i)
						#获取依赖的key
						depend_key = self.data.get_depend_field(i)
						request_data[depend_key] = depend_response_data

					if depend_case_sql != None:
						#获取的sql查询依赖数据
						depend_sql_results = self.data.get_one_sql_data(i, self.data.get_sql_rely_result_data)
						#如果depend_sql_results的值为null说明这段sql语句没有查询出结果，比如我在做某个用户新增之前我需要先删除，
						#但是如果该用户根本都没有的话，那么就删除不了，这时候就需要这里的if来判断
						if depend_sql_results != "null":
							#把unicode格式的字典改为json格式
							depend_sql_results = json.loads(depend_sql_results)
							#通过循环把字典数据里面的value取出来
							for key in depend_sql_results:
								depend_sql_result= depend_sql_results[key]

							#获取依赖的key
							depend_key = self.data.get_depend_field(i)
							request_data[depend_key] = depend_sql_result

					if header == 'write':
						res = self.run_method.run_main(method,url,request_data)
						op_header = OperationHeader(res)
						op_header.write_header()



					elif header == 'yes':
						op_json = OperetionJson('../dataconfig/cookie.json')
						cookie = op_json.get_data('token')
						cookies = {
							"Authorization":cookie
						}
						try:
							res = self.run_method.run_main(method,url,request_data,cookies)
						except json.decoder.JSONDecodeError:
							# 如果出现json.decoder.JSONDecodeError的报错的话，就走到这里，然后把响应的模块清空
							# 这样子的话我就知道哪些模块出错了，或者说知道哪些模块没有执行
							self.data.write_void_to_output_cell(i, " ")
							print(self.data.get_case_name(i))
							continue

					else:
						try:
							res = self.run_method.run_main(method,url,request_data)
						except json.decoder.JSONDecodeError:
							# 如果出现json.decoder.JSONDecodeError的报错的话，就走到这里，然后把响应的模块清空
							# 这样子的话我就知道哪些模块出错了，或者说知道哪些模块没有执行
							self.data.write_void_to_output_cell(i, " ")
							print(self.data.get_case_name(i))
							continue



					#写响应结果返回值到返回状态列
					self.data.write_code_responde_result(i, json.loads(res)['code'])
					#写请求数据内容到请求数据内容列
					self.data.write_request_data_result(i, json.dumps(request_data, ensure_ascii=False))


					#判断预期结果和实际结果是否一致，并将结果填入excel
					if self.com_util.is_equal_dict2(expect,res) == True:
						self.data.write_result_status(i, 'pass')
						self.data.write_result(i, res)
						pass_count.append(i)
					else:
						self.data.write_result_status(i, 'fail')
						self.data.write_result(i,res)
						fail_count.append(i)

					sql_result = self.data.get_all_sql_data(i, self.data.get_sql_result_data)
					self.data.write_sql_result(i, sql_result)
			self.send_mai.send_main(pass_count,fail_count, jsonOfExcelDict)

	#将执行判断封装
	#def get_cookie_run(self,header):


if __name__ == '__main__':
	run = RunTest()
	run.go_on_run()