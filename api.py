import requests
import json

link='https://opentdb.com/api.php?amount=10&category=9&difficulty=easy&type=boolean'

response=requests.get(link)
data=response.json()
results=data['results']
data=[]
for result in results:
    simplified_item = {
        'question':result['question'],
        'correct_answer': result['correct_answer']
    }
    data.append(simplified_item)
