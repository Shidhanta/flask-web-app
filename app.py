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
            print("eng: ",eng, " hind: ",hind)
            if '/' in hind:
                hind1,hind2 = hind.split('/')
                hind1 = hind1.translate(str.maketrans('','',string.punctuation)).lower().strip()
                hind2 = hind2.translate(str.maketrans('','',string.punctuation)).lower().strip()
                l = [eng,hind1,hind2]
                
            else :
                hind = hind.translate(str.maketrans('','',string.punctuation)).lower().strip()
                l = [eng,hind]
                
            hindiphrases.append(l)
            print(hindiphrases)
        except:
            continue

@app.route('/',methods = ['GET','POST'])
def basic():
    with open('user_score.txt','r') as f:
        score = int(f.read())
    loaded_q.append(choice(hindiphrases))
    q = loaded_q[len(loaded_q)-1][0]
    q = f"Translate: {eng}"
    return render_template('index.html',q=q)


app.run(debug=True)

if __name__ == "__main__":
    app.run()