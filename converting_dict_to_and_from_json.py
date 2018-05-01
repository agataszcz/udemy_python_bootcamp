#!/usr/bin/env python
'''
Saving dictionary as a Json string and converting it back to a dictionary.
Printing tweets from a JsonL file.
'''
import json

myd = {'key1': "strawberry", 'key2': "banana", 'key3': 'cherry'}

with open('result.json', 'w+') as f:
	#w = writing mode. The cursor is at the end. The object is not readable yet.
	#w+ = writing and reading mode. The object is now readable. To print its content, set the cursor back at the front (seek(0)).
	#Use json.dumps() to ensure that items inside the Json string have double quotes. Json only accepts double-quoted strings. 
	#Json.loads() will not work with single-quoted strings. 
    f.write(json.dumps(myd))
    f.seek(0)
    content = f.read()
    print(content)


with open('result.json','r') as f:
	#converting Json string back to a dictionary
    newd = json.loads(f.read())
    print(newd)


with open('filepath.jsonl', 'r') as f: 
    #printing texts of tweets saved in Json Lines format (one tweet per line)
    for line in f:
        tweet = json.loads(line)
        print(tweet['text'])
