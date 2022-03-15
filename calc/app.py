# Put your app in here.
from flask import Flask, request
import operations

app = Flask(__name__)


@app.route('/add')
def add():
    a = int(request.args["a"])
    b = int(request.args["b"])
    sum = operations.add(a, b)
    return str(sum)


@app.route('/sub')
def sub():
    a = int(request.args["a"])
    b = int(request.args["b"])
    return str(operations.sub(a, b))


@app.route('/mult')
def mult():
    a = int(request.args["a"])
    b = int(request.args["b"])
    return str(operations.mult(a, b))


@app.route('/div')
def div():
    a = int(request.args["a"])
    b = int(request.args["b"])
    return str(operations.div(a, b))


@app.route('/math/<operand>')
def math(operand):
    a = int(request.args["a"])
    b = int(request.args["b"])
    operand_dict = {"add": operations.add, "sub": operations.sub,
                    "mult": operations.mult, "div": operations.div}

    return str(operand_dict[operand](a, b))
