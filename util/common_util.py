#coding:utf-8
from jsonpath_rw import jsonpath, parse
import json
import operator
class CommonUtil:
	def is_contain(self,str_one,str_two):
		'''
		判断一个字符串是否再另外一个字符串中
		str_one:查找的字符串
		str_two：被查找的字符串
		'''
		flag = None
		if isinstance(str_one, str):
			str_one = str_one.encode('unicode-escape').decode('string_escape')
		return operator.eq(str_one,str_two)
		if str_one in str_two:
			flag = True
		else:
			flag = False
		return flag

	#dict_one是预期结果，dict_two是实际结果
	def is_equal_dict(self,dict_one,dict_two):
		'''
		判断两个字典是否相等
		'''
		if isinstance(dict_one,str):
			dict_one = json.loads(dict_one)
		if isinstance(dict_two,str):
			dict_two = json.loads(dict_two)
		temp = operator.eq(dict_one,dict_two)
		return operator.eq(dict_one,dict_two)

	#dict_one是预期结果，dict_two是实际结果
	def is_equal_dict2(self,dict_one,dict_two):
		'''
		判断两个字典是否相等
		'''
		if isinstance(dict_one,str):
			dict_one = json.loads(dict_one)
		if isinstance(dict_two,str):
			dict_two = json.loads(dict_two)
		#每次默认将boolCheck设置为Flase，如果下面的字典检查全部都相等那么就赋值True
		boolCheck = False
		# 如果dict_one没有数据（也就是说excel表里面这个单元格为空），则返回None
		if dict_one is None:
			return None
		else:
			# 遍历预期结果字典里面所有的key
			for key in dict_one:
				jsonpath_expr = parse('$..' + key)
				# print("key : " + key)
				# 通过期望结果里面的key去找到实际结果里面对应的value，并且将结果生成数组
				matchValueList = [match.value for match in jsonpath_expr.find(dict_two)]
				# print(matchValueList)
				#将预期结果的value和实际结果的value比较，然后用boolCheck记录比较结果
				if len(matchValueList) == 1:
					# print("len等于1")
					# print(matchValueList)
					# 下面五行是用来检验数组里面是否只有一个元素，如果有两个元素的话就会触发except的流程
					# print(matchValueList[0])
					# try:
					# 	print(matchValueList[1])
					# except Exception as e:
					# 	print("数组里面可能只有一个元素, python报错详情如下：\n" + str(e) + "!!!")
					if dict_one[key] == matchValueList[0]:
						# print(dict_one[key], matchValueList[0])
						# print(11233333)
						boolCheck = True
					#如果有一个预期结果的value和实际结果不匹配那么就在给与boolCheck赋值False之后就跳出循环
					else:
						boolCheck = False
						break
				# 有时候会出现响应的字典里面有重复value得情况（也就是说有至少两个key拥有同样的value，
				# 这种情况暂时还不知道该怎么判断，先把这里设置为强行break吧，之后业务流程弄得更熟了再来研究）
				elif len(matchValueList) > 1:
					# print("len大于1")
					break
				# 如果数组里面没有数据的话，则说明预期结果的key没有在实际结果里面发现
				else:
					# print("数据里面没得东西")
					# print(matchValueList)
					break
		return boolCheck


if __name__ == '__main__':
	run = CommonUtil()
	jsonpath_expr = parse('$..bb')
	dict1 = {'code': "100000", "from_company_name": "武汉精臣智慧标识有限公司"}
	dict2 = {"code": "100000", "msg": "请求成功", "data": {"total": 9, "limit": 15, "page": 1, "list": [{"staff_id": 36, "staff_name": "王五", "work_number_prefix": "JC", "work_number": "0098", "work_status": 1, "position_name": "JAVA", "obs_name": "软件部", "certificates_code": ""}, {"staff_id": 34, "staff_name": "第三方", "work_number_prefix": "JC", "work_number": "0024", "work_status": 3, "position_name": "JAVA", "obs_name": "武汉精臣智慧标识有限公司", "certificates_code": ""}, {"staff_id": 31, "staff_name": "ghj", "work_number_prefix": "JC", "work_number": "0916", "work_status": 1, "position_name": "JAVA", "obs_name": "武汉精臣智慧标识有限公司", "certificates_code": ""}, {"staff_id": 29, "staff_name": "快回家", "work_number_prefix": "JC", "work_number": "0914", "work_status": 2, "position_name": "JAVA", "obs_name": "武汉精臣智慧标识有限公司", "certificates_code": ""}, {"staff_id": 18, "staff_name": "张三丰", "work_number_prefix": "JC", "work_number": "0911", "work_status": 3, "position_name": "JAVA", "obs_name": "软件部", "certificates_code": "421012199005011211"}, {"staff_id": 17, "staff_name": "test1", "work_number_prefix": "JC", "work_number": "0099", "work_status": 2, "position_name": "JAVA", "obs_name": "软件部", "certificates_code": ""}, {"staff_id": 16, "staff_name": "测试员工2", "work_number_prefix": "JC", "work_number": "0005", "work_status": 3, "position_name": "JAVA", "obs_name": "354345", "certificates_code": "421023199521451236"}, {"staff_id": 6, "staff_name": "曾凡华", "work_number_prefix": "JC", "work_number": "0002", "work_status": 2, "position_name": "JAVA", "obs_name": "软件部", "certificates_code": ""}, {"staff_id": 1, "staff_name": "jessezhang", "work_number_prefix": "JC", "work_number": "0001", "work_status": 3, "position_name": "JAVA", "obs_name": "武汉精臣智慧标识有限公司", "certificates_code": ""}]}}
	dict3 = {"code": "100000", "msg": "请求成功", "data": {"total": 1, "limit": 15, "page": 1, "list": [
		{"user_id": 5, "staff_id": 19, "staff_name": "rty", "work_numbers": "JC0912", "mobile": "13237150922",
		 "obs_name": "武汉精臣智慧标识有限公司", "from_company_name": "武汉精臣智慧标识有限公司", "isno_company": 1, "obs_names": "",
		 "position_name": "gh", "work_status": 1, "role_name_str": "人事专员,物品管理员,aa副本,测试角色2副本,考勤专员,aa副本副本",
		 "isno_super_admin_str": "0",
		 "company_name_str": "313,jesseTest部门添加23,rtyrtyryyuijjj,技术,asadasd,cvvvvvvvv,研发,dfgdfg,qwqqqq,研发a",
		 "isno_super_admin": 0}]}}
	check = run.is_equal_dict2(dict1, dict3)
	print(check)