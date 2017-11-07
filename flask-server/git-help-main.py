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

	print(data)

	"""jsonlist = []
	scores = {} # init empty scores list
	for row in rows: # iterates and adds to scores
		score_json = {}
		score_json['name'] = row[0]
		score_json['score'] = row[1]

		jsonlist.append(score_json)"""

	return jsonify(data=data)

app.run(host="0.0.0.0", port="5000")
