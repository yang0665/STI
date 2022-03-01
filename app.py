# -*- coding: utf-8 -*-
"""
Created on Tue Mar  1 20:12:16 2022

@author: Daisy
"""

from flask import Flask
app = Flask(__name__)

import joblib
from flask import request, render_template 
@app.route("/", methods = ["GET","POST"] )

def index():
    if request.method == "POST":
        Nikkei = request.form.get("Nikkei")
        print(Nikkei)
        model1 = joblib.load("STI_REG")
        pred1 = model1.predict([[Nikkei]])
        str1 = "The prediction for STI using regression is: " + str(pred1)
        return (render_template("index.html", result1= str1))
    else:
        return(render_template("index.html", result1 = "2"))

if __name__ =="__main__":
    app.run()
    