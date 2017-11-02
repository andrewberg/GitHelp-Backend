import json
from pprint import pprint

with open('../lessons/lessonsch5.json') as data_file:    
    data = json.load(data_file)

pprint(len(data['lesson']))