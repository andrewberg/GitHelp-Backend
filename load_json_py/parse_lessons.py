import json
from os import listdir
from pprint import pprint

# lesson object to convert from JSON

class Lesson:
	
	"""Lesson object for JSON conversion then input to MySQL"""
	def __init__(self, chapter, lesson, title, body):
		self.chapter = chapter
		self.lesson = lesson
		self.title = title
		self.body = body

class Lessons:
	
	"""Lessons object to hold Lesson objects"""
	def __init__(self):
		self.lessons = []

	"""Adds Lesson to array to store it"""
	def add_lesson(self, lesson):
		self.lessons.add(lesson)

	"""Write all the Lesson objects to the MySQL database"""
	def write_to_db(self):
		print("TODO:")


# sorts the list so that it reads the list properly
directory_list = sorted(listdir('../lessons/'))

# defines data for storage
data = []

# loops through the directory_list
#for file in xrange(2,3):

	# opens the file and loads the JSON in from each of the files
#	with open('../lessons/' + directory_list[file]) as data_file:    
#	    data.append(json.load(data_file))

# temporary because 1-6 is not complete data yet

with open('../lessons/lessonsch1.json') as data_file:
	data.append(json.load(data_file))

with open('../lessons/lessonsch2.json') as data_file:
	data.append(json.load(data_file))

with open('../lessons/lessonsch3.json') as data_file:
	data.append(json.load(data_file))

with open('../lessons/lessonsch4.json') as data_file:
	data.append(json.load(data_file))

with open('../lessons/lessonsch5.json') as data_file:
	data.append(json.load(data_file))

# extracts the lesson from the lesson dictionary part of the data

for val in xrange(len(data)):

	# extracts the lesson from the JSON dictionary
	lessons_ch = data[val]['lesson']

	# loop to go through each and add to the list of the chapter that we are on
	data[val] = lessons_ch

# go through data and add it to the MySQL database

for chapter in xrange(len(data)):
	for lesson in xrange(len(data[chapter])):
		
		# extracting the values from the JSON array
		
		print(str(chapter) + '.' + str(lesson))

		title = data[chapter][lesson]['title']
		body = data[chapter][lesson]['body']
		
		