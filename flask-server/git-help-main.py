from flask import Flask
from flask import jsonify

import MySQLdb

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/lessons')
def print_lessons():
	conn = MySQLdb.connect(host="localhost", user="root", passwd="engineering",db="githelp")
	x = conn.cursor()

	data = ""

	try:
	   x.execute("""SELECT * FROM Lesson""")
	   data = x.fetchall()
	except Exception as e:
		print(e)
	   	conn.rollback()

	return jsonify(data=data)

@app.route('/quizzes')
def print_quizzes():
	conn = MySQLdb.connect(host="localhost", user="root", passwd="engineering",db="githelp")
	x = conn.cursor()

	data = ""

	try:
	   #x.execute("""SELECT * FROM QuizQuestion as qq LEFT JOIN QuizChoices as qc on qq.questionID = qc.questionID
	   	#			UNION
	   	#			SELECT * FROM QuizQuestion as qq RIGHT JOIN QuizChoices as qc on qq.questionID = qc.questionID""")
	   
	   	
	   data = x.fetchall()
	except Exception as e:
		print(e)
	   	conn.rollback()

	return jsonify(data=data)

app.run(host="0.0.0.0", port="5000")
