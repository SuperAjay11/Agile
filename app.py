from flask import Flask,  render_template, request
import random
import sys

app = Flask(__name__)

@app.route("/", methods =['POST', 'GET'])
def home():
    return render_template("index.html")
        
def submit():
    usrinput = request.form['usrinput']
    list = []
    list.append(usrinput)
    return list

def random():
    random_value = random.choice(list)
    return render_template("index.html", random_value)
    

if __name__ == "__main__":
    app.run()