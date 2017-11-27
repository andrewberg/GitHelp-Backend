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


	lesson = []

	for row in data:
		lesson_json = {}
		lesson_json['title'] = row[3]
		lesson_json['body'] = row[4]

		lesson.append(lesson_json)

	
	return jsonify({'lessons':lesson})

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
	answers = []

	"""for row in data:
		if (int(row[2]) is cur_question):
			cur_choices.append(row[5])
		else:
			cur_question += 1
			question_choices.append(cur_choices)
			cur_choices = []
			questions.append(row[1])
			answers.append(int(row[4]))


	chapters = []
	question = {}
	questions_dic = []
	cur_question = 0
	for row in data:
		print(row)
		if int(row[0]) is cur_chapter and cur_question < len(questions):
			question['text'] = questions[cur_question]
			question['choices'] = question_choices[cur_question]
			question['answer'] = answers[cur_question]
			questions_dic.append(question)
			question = {}
			cur_question += 1
		else:
			cur_chapter += 1
			chapters.append(questions_dic)
			questions = {}"""
	
	"""need to go through each different question and add it to the dictionary
		then I need to jsonify this data and print it out
	cur_chapter = 0
	for questions in chapters:
		print(cur_chapter)
		cur_chapter += 1
		for question in questions:
			print(question['text'])"""


	return jsonify(data=data)

app.run(host="0.0.0.0", port="5000")
