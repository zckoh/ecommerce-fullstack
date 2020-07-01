from django.db import models
import os
import json

# fetch static data stored in json
def toys_product_list():
    filename = os.path.dirname(os.path.realpath(__file__)) + os.path.sep + \
        'data' + os.path.sep + 'toys' + os.path.sep + 'product_list.json'

    with open(filename) as product_list:
        products = json.load(product_list)
    return products


def copybooks_product_list():
    filename = os.path.dirname(os.path.realpath(__file__)) + os.path.sep + \
        'data' + os.path.sep + 'copybooks' + os.path.sep + 'product_list.json'

    with open(filename) as product_list:
        products = json.load(product_list)
    return products

def pens_product_list():
    filename = os.path.dirname(os.path.realpath(__file__)) + os.path.sep + \
        'data' + os.path.sep + 'pens' + os.path.sep + 'product_list.json'

    with open(filename) as product_list:
        products = json.load(product_list)
    return products