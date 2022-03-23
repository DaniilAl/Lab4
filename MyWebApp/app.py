from flask import Flask, render_template

app = Flask(__name__)

@app.route('/login/', methods=['GET'])
def index():
    return render_template('login.html')
