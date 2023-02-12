# import the package
from flask import Flask, abort
from data import me, mock_database
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

@app.get("/api/products")
def products():
    # string = mock_database
    # apples = string[0]["title"],string[0]["category"],string[0]["price"]
    # oranges = string[1]["title"],string[1]["category"],string[1]["price"]
    # bananas = string[2]["title"],string[2]["category"],string[2]["price"]
    # pears = string[3]["title"],string[3]["category"],string[3]["price"]
    # grapes = string[4]["title"],string[4]["category"],string[4]["price"]
    # carrots = string[5]["title"],string[5]["category"],string[5]["price"]
    # celery = string[6]["title"],string[6]["category"],string[6]["price"]
    # return f'{apples,oranges,bananas,pears,grapes,carrots,celery}'
    return json.dumps(mock_database)

@app.get("/api/products/count")
def products_count():
    length = len(mock_database)
    return json.dumps(length)

@app.get("/api/categories/<category>")
def categories(category):
    # in class
    # results = []
    # for product in mock_database:
    #     if product["category"] == category:
    #         results.append(product)
    # return json.dumps(results)
    filtered = list(filter(lambda x: x["category"] == category, mock_database))
    return json.dumps(filtered)

@app.get("/api/product/<_id>")
def product(_id):
    filtered = list(filter(lambda x: x["_id"] == _id, mock_database))
    if len(filtered) == 0:
            return abort(404, "Not found")
    else:
            return json.dumps(filtered)

@app.get("/api/product/search/<search>")
def product_search(search):
    filtered = list(filter(lambda x: search.lower() in x["title"].lower(), mock_database))
    if len(filtered) == 0:
            return abort(404, "Not found")
    else:
            return json.dumps(filtered)

@app.get("/api/unique_categories")
def unique_categories():
    categories = []
    for product in mock_database:
        if product["category"] not in categories:
            categories.append(product["category"])
    return json.dumps(categories)

@app.get("/api/total")
def total():
    total = 0
    for product in mock_database:
        total += product["price"]
    return json.dumps(total)

@app.get("/api/cheaper/<price>")
def cheaper(price):
    cheap = []
    for product in mock_database:
        if product["price"] <= float(price):
            cheap.append(product)
    return json.dumps(cheap)

@app.get("/api/cheapest")
def cheapest_product():
    cheapest = mock_database[0]
    for product in mock_database:
        if product["price"] < cheapest["price"]:
            cheapest = product
    return json.dumps(cheapest)
# ###############################################
# api -> json
# ###############################################

@app.get("/api/dev")
def dev():
    return json.dumps(me)

@app.get("/api/dev/address")
def dev_address():
    string = me["address"]
    return f'{string["street"]} #{string["number"]}, {string["zipcode"]} {string["city"]}'

app.run(debug=True)