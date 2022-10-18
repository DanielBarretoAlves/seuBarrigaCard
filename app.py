from flask import Flask, render_template, request, redirect
from flask import Flask

def index():
    pronto = {}
    pronto['cliente.ID'] = 99999


app = Flask(__name__)

@app.route("/", methods=["GET"])
def home():
    return render_template('index.html')

@app.route("/donos", methods=["GET"])
def dono():
    return render_template('dono.html')


@app.route('/dono')
def show_form():
    return render_template('dono.html')



@app.route("/result", methods=['POST'])
def show_result():
    result = request.form
    return render_template('dono.html', result=result)