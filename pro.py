# -*- coding:utf-8 -*- 
from flask import Flask,request,render_template,redirect,url_for,jsonify
import json
from MySQLProcess import MySQLProcessor

app=Flask(__name__)

dept_num={}
Db_processor=MySQLProcessor("","")

@app.route('/')
def show_index():
	return render_template('index.html')


@app.route('/search',methods=['POST','GET'])
def search():
	if request.method == 'POST':
		data = request.form.get('num')
		sign=not dept_num.has_key('num')
		if sign:
			dept_num['num']=str(data)
			dept_num['num']=dept_num['num'].encode("utf8")

	if request.method == 'GET':
		data = request.args.get('name')
		print data
		if isinstance(data,unicode):
			data=data.encode('utf8')
			Db_processor=MySQLProcessor(dept_num['num'],data)
			hints=Db_processor.queryHints_db('select')
			print hints
			return jsonify(matching_results=hints)
	return render_template('search.html')
if __name__ == '__main__':
	app.run()