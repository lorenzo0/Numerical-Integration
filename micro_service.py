from numerical_integration import numerical_integration
from flask import Flask

app = Flask(__name__)

@app.route("/<lower>/<upper>")
def app_numerical_integration(lower, upper):
    print("Values: "+lower + " - " + upper)
    return ("Final value: " +numerical_integration(float(lower), float(upper)))

