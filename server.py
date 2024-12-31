from flask import Flask, render_template, jsonify, request
import json

app = Flask(__name__)

records = []

@app.route('/')
def home():
    return render_template('index.html')

# Get history
# curl -X GET http://localhost:5000/api
@app.route('/api')
def get_all():
    return records

# curl -X POST -d "addend1=3.5&addend2=2.4" http://localhost:5000/api/add
@app.route('/api/add', methods=['POST'])
def add_record():
    addend1 = request.form.get('addend1')
    addend2 = request.form.get('addend2')
    sum = float(addend1) + float(addend2)
    sum = f"{sum:.2f}"
    response = addend1 + " + " + addend2 + " = " + sum
    records.append(response)
    return response

# curl -X POST -d "minuend=5.5&subtrahend=2.2" http://localhost:5000/api/subtract
@app.route('/api/subtract', methods=['POST'])
def subtract_record():
    minuend = request.form.get('minuend')
    subtrahend = request.form.get('subtrahend')
    difference = float(minuend) - float(subtrahend)
    difference = f"{difference:.2f}"
    response = minuend + " - " + subtrahend + " = " + difference
    records.append(response)
    return response

# curl -X POST -d "factor1=2&factor2=3" http://localhost:5000/api/multiply
@app.route('/api/multiply', methods=['POST'])
def multiply_record():
    factor1 = request.form.get('factor1')
    factor2 = request.form.get('factor2')
    product = float(factor1) * float(factor2)
    product = f"{product:.2f}"
    response = factor1 + " * " + factor2 + " = " + product
    records.append(response)
    return response

# curl -X POST -d "dividend=12&divisor=3" http://localhost:5000/api/divide
@app.route('/api/divide', methods=['POST'])
def divide_record():
    dividend = request.form.get('dividend')
    divisor = request.form.get('divisor')
    quotient = float(dividend) / float(divisor)
    quotient = f"{quotient:.2f}"
    response = dividend + " / " + divisor + " = " + quotient
    records.append(response)
    return response

# curl -X POST -d "base=5&exponent=3" http://localhost:5000/api/power
@app.route('/api/power', methods=['POST'])
def power_record():
    base = request.form.get('base')
    exponent = request.form.get('exponent')
    result = float(base) ** float(exponent)
    result = f"{result:.2f}"
    response = base + " ^ " + exponent + " = " + result
    records.append(response)
    return response

if __name__ == '__main__':
    app.run(debug=True)