from flask import Flask, request,render_template


app=Flask(__name__)

@app.route("/calculate")

def calculate():
    bmi=''
    Weight=float(request.form.get('weight'))
    Height=float(request.form.get('weight'))

    return render_template("index.html")