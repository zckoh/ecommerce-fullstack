from django.db import models
import os
import json

# fetch static data stored in json
def get_product_list():
    filename = os.path.dirname(os.path.realpath(__file__)) + os.path.sep + \
        'data' + os.path.sep + 'product_list.json'

    with open(filename) as product_list:
        products = json.load(product_list)
    return products