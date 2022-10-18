import json
from flask import Flask, render_template, request, redirect
from flask import Flask, jsonify, json


def index():
    pronto = {}
    pronto['cliente.ID'] = 99999


app = Flask(__name__)


@app.route("/dada", methods=["GET"])
def home():
    return render_template('index.html')


@app.route("/test", methods=["POST", "GET"])
def dono():
    valor = request.form.get('valor')
    pagamento = request.form.get('mtdPagamento')
    
    # "Forma De Pagamento " + pagamento + " Valor a Pagar" + valor 
    return  redirect('index.html')
    

@app.route('/')
def show_form():
    # Console.log("teste1")
    return render_template('dono.html')


# @app.route("/result", methods=['POST'])
# def show_result():
#     print("here")
#     result = request.form
#     # console.log(result)
#     return render_template('dono.html', result=result)
