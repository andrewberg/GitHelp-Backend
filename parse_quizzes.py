import json
import MySQLdb
import io
from os import listdir
from pprint import pprint

# lesson object to convert from JSON

class Quiz:
	
	"""Quiz object for JSON conversion then input to MySQL"""
	def __init__(self, chapter, text, id, answer, choices):
		self.chapter = chapter
		self.text = text
		self.id = id
		self.answer = answer
		self.choices = choices

class Quizzes:
	
	"""Quizzes object to hold Quiz objects"""
	def __init__(self):
		self.quizzes = []

	"""Adds Lesson to array to store it"""
	def add_quiz(self, quiz):
		self.quizzes.append(quiz)

	"""Write all the Lesson objects to the MySQL database"""
	def write_to_db(self):
		conn = MySQLdb.connect(host="localhost", user="root", passwd="engineering",db="githelp")
		x = conn.cursor()
		
		x.execute("""TRUNCATE TABLE QuizQuestion""")
		x.execute("""TRUNCATE TABLE QuizChoices""")

		for quiz in self.quizzes:
			try:
			   x.execute("""INSERT INTO QuizQuestion (chapter, questionText, questionID, questionAnswer) VALUES (%s,%s,%s,%s)""", (quiz.chapter,quiz.text,quiz.id,quiz.answer))
			   conn.commit()

			   for choice in quiz.choices:
			   	try:
			   		x.execute("""INSERT INTO QuizChoices (text, questionID) VALUES (%s, %s)""", (choice, quiz.id))
			   		conn.commit()
			   	except Exception as e:
					print(e)
				   	conn.rollback()
			except Exception as e:
				print(e)
			   	conn.rollback()


# sorts the list so that it reads the list properly
directory_list = sorted(listdir('./quizzes/'))

# defines data for storage
data = []

# define the Lessons object

quizzes = Quizzes()

# loops through the directory_list
#for file in xrange(2,3):

	# opens the file and loads the JSON in from each of the files
#	with open('./lessons/' + directory_list[file]) as data_file:    
#	    data.append(json.load(data_file))

# temporary because 1-6 is not complete data yet

with open('./quizzes/quiz1.json') as data_file:
	data.append(json.load(data_file))

with open('./quizzes/quiz2.json') as data_file:
	data.append(json.load(data_file))

with open('./quizzes/quiz3.json') as data_file:
	data.append(json.load(data_file))

with open('./quizzes/quiz4.json') as data_file:
	data.append(json.load(data_file))

with open('./quizzes/quiz5.json') as data_file:
	data.append(json.load(data_file))

with open('./quizzes/quiz6.json') as data_file:
	data.append(json.load(data_file))

with open('./quizzes/quiz7.json') as data_file:
	data.append(json.load(data_file))

with open('./quizzes/quiz8.json') as data_file:
	data.append(json.load(data_file))

with open('./quizzes/quiz9.json') as data_file:
	data.append(json.load(data_file))

with open('./quizzes/quiz10.json') as data_file:
	data.append(json.load(data_file))

# extracts the lesson from the lesson dictionary part of the data

for val in xrange(len(data)):

	# extracts the lesson from the JSON dictionary
	quizzes_ch = data[val]['quiz']['questions']

	# loop to go through each and add to the list of the chapter that we are on
	data[val] = quizzes_ch


# go through data and add it to the MySQL database

q_num = 0
c_num = 0

for val in xrange(len(data)):
	for x in xrange(len(data[val])):

		text = data[val][x]['text']
		index = data[val][x]['index']
		choices = data[val][x]['choices']

		quiz = Quiz(c_num, text, q_num, index, choices)
		quizzes.add_quiz(quiz)

		q_num += 1
	c_num += 1

quizzes.write_to_db()


