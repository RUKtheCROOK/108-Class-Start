# import the package
from flask import Flask
from data import me
import json

app = Flask(__name__)

@app.get("/")
def home():
    return "Hello World"

@app.get("/about")
def about():
    return "About Page"

@app.get("/contact/me")
def contactme():
    return "MyEmailAddress@gmail.com"



# ###############################################
# api -> json
# ###############################################

@app.get("/api/dev")
def dev():
    return json.dumps(me)

@app.get("/api/dev/address")
def dev_address():
    string = me["address"]
    # return string ["street"] + str(string["number"]) + string["zipcode"] + string["city"]
    return f'{string["street"]} #{string["number"]}, {string["zipcode"]} {string["city"]}'

app.run(debug=True)