# -*- coding:utf-8 -*-  
import MySQLdb,json

class MySQLProcess():
	table=""
	target=""
	db=""
	def __init__(self,dept_num,target):
		self.db=MySQLdb.connect(host='localhost',user='root',passwd='abysmaN169',db='Scrapy_Test')
		self.cur=self.db.cursor()
		self.table='Test_'+dept_num+'b'
		self.target=target

	def queryHints_db(self,query):
		if query[0:6].lower() == 'select':
			sql = "SELECT DISTINCT DATA_POST from %s where DATA_POST LIKE '%%%s%%'"%(self.table,self.target)
			self.cur.execute(sql)
			select_result = self.cur.fetchall()
		if query[0:6].lower() == 'insert':
			sql = ""
			self.cur.execute(sql)
		# 转换为json格式
		jsonData=[]
		for row in select_result:
			result={}
			result['value']=row[0]
			jsonData.append(result)
		jsonResult=json.dumps(jsonData,ensure_ascii=False)
		self.db.commit()
		self.cur.close()
		self.db.close()
		return jsonResult

def MySQLProcessor(table,target):
	return MySQLProcess(table,target)

a=MySQLProcessor('0155','a')
print a.table
print a.target
result=a.queryHints_db('select')
print result


		