from flask import Flask,render_template,request
from random import choice
import string 

app = Flask(__name__)

loaded_q = []
hindiphrases = []
with open('user_score.txt','w') as f:
    f.write(str(0))

with open('hindiphrases.txt','r') as f:
    for line in f:
        try:
            
            line = line.strip('\n')
            eng,hind = line.split('-')
            if '/' in hind:
                hind1,hind2 = hind.split('/')
                hind1 = hind1.translate(str.maketrans('','',string.punctuation)).lower().strip()
                hind2 = hind2.translate(str.maketrans('','',string.punctuation)).lower().strip()
                l = [eng,hind1,hind2]
                
            else :
                hind = hind.translate(str.maketrans('','',string.punctuation)).lower().strip()
                l = [eng,hind]
                
            hindiphrases.append(l)
        except:
            continue

def load_question():
    loaded_q.append(choice(hindiphrases))
    print("loaded_ q: ",loaded_q)
    eng = loaded_q[len(loaded_q)-1][0]
    q = f"Translate: {eng}"
    return q


@app.route('/',methods = ['GET','POST'])
def basic():
    with open('user_score.txt','r') as f:
        score = int(f.read())
    good = False
    response = ""
    q = load_question()
    if request.method == 'POST':
        if(request.form['text']):
            t = request.form['text'].lower().translate(str.maketrans('','',string.punctuation)).strip()
            # first check how many answers we have; if 2, check if answer is there
            # Note becauase Python is zero-indexed we are getting the previous index of our list with -2
            
            for i in loaded_q[len(loaded_q)-2][1:]:
                if t == i:
                    good = True
            if good:
                response = "Excellent!"
                with open('user_score.txt','r') as f:
                    score = int(f.read())
                    score+=1
                with open('user_score.txt','w') as f:
                    f.write(str(score))
            else:
                response = f"Sorry, try again!"

    return render_template('index.html',q=q,response = response,score=score)        

app.run(debug=True)

if __name__ == "__main__":
    app.run()