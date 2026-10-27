from flask import Flask, render_template
from flask_bootstrap import Bootstrap5

app = Flask(__name__)
bootstrap = Bootstrap5(app)

@app.route('/')
def hello():
    return '<p>Estrella O:YOLO (You only live once)</p> <br> <p>Pedro A: STFU (shut the f up) </p> <br> <p>Lucy B: RBF (resting B face)</p>'

# @app.route('/welcome')
# def wc():
#     s1 = 'Welcome to my page1'
#     s2 = "have a nice day!"
#     return s1 + s2

# @app.route('/my_template')
# def t_test():
#     return render_template('index.html', message = 'Hello from flask!')

@app.route('/lesly')
def me():
    return render_template('index.html', message= "My fave acronym: TGIF")

@app.route('/img')
def img():
    return render_template('task4.html')