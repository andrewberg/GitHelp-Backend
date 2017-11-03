import json
from os import listdir
from pprint import pprint

# sorts the list so that it reads the list properly
directory_list = sorted(listdir('../quizzes/'))

# defines data for storage
data = []

# loops through the directory_list
for file in xrange(1):

	# opens the file and loads the JSON in from each of the files
	with open('../quizzes/' + directory_list[file]) as data_file:    
	    data.append(json.load(data_file))

pprint(data[0]['quiz']['questions'][0])
