from flask import Flask,template_rendered,request
from random import choice
import string 

app = Flask(__name__)

loaded_q = []

with open('user_score.txt','w') as f:
    f.write(str(0))

def basic():
    with open('user_score.txt','r') as f:
        score = int(f.read())
    loaded_q.append(choice(hindiphrases))
    q = loaded_q[len(loaded_q)-1][0]
    q = f"Translate: {eng}"
    return q


