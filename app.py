from re import I
from flask import Flask, render_template, url_for, request
from models.random_output import user_input, word_list, random_output

app = Flask(__name__)

 

@app.route('/')
@app.route('/home')
def home():
    return render_template("index.html")

words = []

@app.route('/result',methods=['POST', 'GET'])
def result():

    usr_input = ""
    words.append(request.form['name'])
    for i in words:
        usr_input += i 

    list = word_list(usr_input)

    

    task = random_output(list)

    


    return render_template('index.html', task = task)
    




if __name__ == "__main__":
    app.run(debug=True)