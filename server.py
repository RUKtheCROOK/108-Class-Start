# import the package
from flask import Flask, abort, request
from data import me, mock_database
from config import db
from bson import ObjectId
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

def fix_id(obj):
    obj["_id"] = str(obj["_id"])
    return obj

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
    cursor = db.products.find({})
    product_list = []
    for product in cursor:
        fix_id(product)
        product_list.append(product)
    return json.dumps(product_list)

@app.post("/api/products")
def products_post():
    data = request.get_json()
    db.products.insert_one(data)
    fix_id(data)

    return json.dumps(data)

@app.get("/api/products/count")
def products_count():
    length = db.products.count_documents({})
    return json.dumps(length)

@app.get("/api/categories/<category>")
def categories(category):
    # in class
    # results = []
    # for product in mock_database:
    #     if product["category"] == category:
    #         results.append(product)
    # return json.dumps(results)
    cursor = db.products.find({"category": category})
    product_list = []
    for product in cursor:
        fix_id(product)
        product_list.append(product)
    # filtered = list(filter(lambda x: x["category"] == category, mock_database))
    return json.dumps(product_list)

@app.get("/api/product/<id>")
def product(id):
    # filtered = list(filter(lambda x: x["_id"] == _id, mock_database))
    _id = ObjectId(id)
    product = db.products.find_one({"_id": _id})

    if product is None:
            return abort(404, "Not found")
    else:
        fix_id(product)
        return json.dumps(product)

@app.get("/api/product/search/<search>")
def product_search(search):
    cursor = db.products.find({"title":{"$regex" : search, "$options" : "i"}})
    product_list = []
    for product in cursor:
        fix_id(product)
        product_list.append(product)
    return json.dumps(product_list)
    # filtered = list(filter(lambda x: search.lower() in x["title"].lower(), mock_database))
    # return json.dumps(filtered)

@app.get("/api/unique_categories")
def unique_categories():
    # categories = []
    # for product in mock_database:
    #     if product["category"] not in categories:
    #         categories.append(product["category"])
    cursor = db.products.distinct("category")
    return json.dumps(cursor)

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