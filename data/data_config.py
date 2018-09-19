#coding:utf-8
class global_var:
	#case_id
	Id = '0'
	request_name = '1'
	url = '2'
	run = '3'
	request_way = '4'
	header = '5'
	case_depend = '6'
	data_depend = '7'
	data_depend_sql= '8'
	field_depend = '9'
	data = '10'
	json_path = '11'
	expect = '12'
	get_sql_result = '13'
	write_sql_result = '14'
	code_responde_result = '15'
	result_status = '16'
	request_data_result = '17'
	responde_result = '18'

#获取case id
def get_id():
	return global_var.Id

#获取case name
def get_name():
	return global_var.request_name

#获取url
def get_url():
	return global_var.url

def get_run():
	return global_var.run

def get_run_way():
	return global_var.request_way

def get_header():
	return global_var.header

def get_header_value():
	return global_var.header

def get_case_depend():
	return global_var.case_depend

def get_data_depend():
	return global_var.data_depend

#依赖的返回数据sql,该列用来存储可能被用来当做依赖的sql里面抓取回来的数据
def get_data_depend_sql():
	return global_var.data_depend_sql

def get_field_depend():
	return global_var.field_depend

def get_data():
	return global_var.data

#通过这一列的帮助，就可以更好的组织json文件的结构了，通过把data写在不同的json文件里面更好的管控接口块
def get_json_path():
	return global_var.json_path

def get_expect():
	return global_var.expect

#这一列用来保存数据库里面查询出来的数据，主要是用来辅助查看编辑和删除的操作是否生效了
def get_sql_result():
	return global_var.get_sql_result

def write_sql_result():
	return global_var.write_sql_result

def get_code_responde_result():
	return global_var.code_responde_result

#测试结果
def get_result_status():
	return global_var.result_status

#请求数据结果
def get_request_data_result():
	return global_var.request_data_result

#实际响应结果
def get_responde_result():
	return global_var.responde_result

