
from os import name
from typing import NamedTuple
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    bmi = ''
    if request.method == 'POST' and 'weight' in request.form:
        Weight = float(request.form.get('weight'))
        Height = float(request.form.get('height'))
        bmi = calc_bmi(Weight, Height)
    return render_template("bmi_calc.html",
	                        bmi=bmi,
                            name=NamedTuple)

def calc_bmi(weight, height):
    return round((weight / ((height / 100) ** 2)), 2)

if __name__ == '__main__':
    app.run()