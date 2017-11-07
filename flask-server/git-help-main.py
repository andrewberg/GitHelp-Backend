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
	   x.execute("""SELECT qq.chapter, qq.questionText, qq.questionID, qq.questionID, qq.questionAnswer, qc.text, qc.questionID FROM QuizQuestion as qq, QuizChoices as qc WHERE qq.questionID = qc.questionID """)
	   

	   data = x.fetchall()
	except Exception as e:
		print(e)
	   	conn.rollback()

	jsonlist = []
	cur_chapter = 0
	cur_question = 0

	question_choices = []
	cur_choices = []
	questions = []

	for row in data:
		if (int(row[2]) is cur_question):
			print('true')
			cur_choices.append(row[5])
		else:
			cur_question += 1
			#print('poop')
			question_choices.append(cur_choices)
			cur_choices = []
			questions.append(row[1])


	print(questions)



	return jsonify(data=data)

app.run(host="0.0.0.0", port="5000")
