#coding:utf-8
import datetime
import json
import requests
from util.operation_json import OperetionJson

class RunMethod:
	def post_main(self, url, data, header=None):
		res = None
		if header !=None:
			res = requests.post(url=url,json=data, headers=header)
			# 输出相应code，如果是4xx，5xx就是说明有问题
			print(res.status_code)
			# print(type(res.status_code))
			print("finished")
			self.check400500err(url, res)
			print("")
		else:
			res = requests.post(url=url,json=data)
			# 输出相应code，如果是4xx，5xx就是说明有问题
			print(res.status_code)
			# print(type(res.status_code))
			print("finished")
			self.check400500err(url, res)
			print("")
		return res.json()

	def get_main(self,url,data=None,header=None):
		res = None
		if header !=None:
			res = requests.get(url=url,params=data,headers=header,verify=False)
			# 输出相应code，如果是4xx，5xx就是说明有问题
			print(res.status_code)
			# print(type(res.status_code))
			print("finished")
			self.check400500err(url, res)
			print("")
		else:
			res = requests.get(url=url,params=data,verify=False)
			#输出相应code，如果是4xx，5xx就是说明有问题
			print(res.status_code)
			# print(type(res.status_code))
			print("finished")
			self.check400500err(url, res)
			print("")
		return res.json()

	def run_main(self, method, url, data=None, header=None):
		res = None
		if method.capitalize() == 'Post':
			res = self.post_main(url,data,header)
		else:
			res = self.get_main(url,data,header)
		return json.dumps(res,ensure_ascii=False)
		#return json.dumps(res,ensure_ascii=False,sort_keys=True,indent=2)

	def check400500err(self, url, res):
		# 如果接口编码响应为5xx或者4xx的话，就把该接口url和该编码写入到dataconfig夹子下的err500list.txt文件
		if str(res.status_code)[0] == "4" or str(res.status_code)[0] == "5" or str(res.status_code)[0] == "":
			with open(r"../dataconfig/err500list.txt", "a+") as err500list:
				# self.setExcelPathName("测试测试")
				new_500_error = '---------\n' + self.getExcelPathName() + '\n' + str(datetime.datetime.now()) + '\n' + str(res.status_code) + '\n' + url + '\n'
				err500list.write(new_500_error)

	def getExcelPathName(self):
		return self.excelPathName

	def setExcelPathName(self, excelPathName):
		self.excelPathName = excelPathName







if __name__ == '__main__':
	op_json = OperetionJson('../dataconfig/cookie.json')
	cookie = op_json.get_data('token')
	headers = {
        "Content-Type": "application/json",
		"Authorization":cookie
	}

	createobs1Url = 'http://oa.jc-saas.com.cn/obs/add'
	cba1= {
		"parent_id": '4',
		"obs_name": "jesseTest部门添加23",
		"isno_company": '1',
		"obs_abbreviation": "",
		"duty_staff_work_number": "",
		"establish_time": "",
		"plan_staff_num": "",
		"note": "",
		"company_name": "",
		"company_type": "",
		"industry_name": "",
		"administrative_code": "",
		"duty_paragraph": "",
		"business_license_code": "",
		"approval_code": "",
		"juridical_entity_code": "",
		"legal_person": "",
		"legal_person_idcard": ""
	}

	login= {
		"work_number": "jc0001",
		"password": "123456",
	}

	voidAll =  {
		"role_id": "81",
		"company_id": "1",
		"role_name": "测试1",
		"role_note": ""
	}
	voidAll =  {
		"staff_id": "1",
		"contract_type": "2",
		"contract_number": "2222",
		"contract_company": 2,
		"date_signing": "2012-12-12",
		"contract_start_time": "2012-12-12",
		"note": "test contract edit",
		"staff_contract_id": ""
	}
	url111="http://oa.jc-saas.com.cn/staff/Contract/add"


	createPosition1 = "http://oa.jc-saas.com.cn/position/detail"
	createPosition1Data = {"position_id": "2"}

	error500Test = "http://oa.jc-saas.com.cn/obs/import"
	error500TestData = {"": ""}

	testUpload = "http://oa.jc-saas.com.cn/attendance/daily/import"


	checkRedundantName = "http://oa.jc-saas.com.cn/obs/nameCheck"
	checkRedundantNameData = {"parent_id": "1", "obs_name": "软件部", "obs_id": ""}


	run_method = RunMethod()
	res = run_method.run_main('post', url111, voidAll, headers)
	print(res)