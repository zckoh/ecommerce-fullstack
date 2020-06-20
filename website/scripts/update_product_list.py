import json
import sys
import os
from algoliasearch.search_client import SearchClient

# This script updates the product list in products/data/product_list.json
# This is done by downloading the data from algolia index and replacing the product_list.json with the new content.
def main():
    product_list_filepath = os.getcwd() + "/products/data/product_list.json"

    print("Updating the product list: " + product_list_filepath)

    client = SearchClient.create('9SXIDIVU1E', os.environ['ALGOLIA_ADMIN_API_KEY'])
    index = client.init_index('products_index')

    hits = []

    for hit in index.browse_objects({'query': ''}):
        hits.append(hit)

    with open(product_list_filepath, 'w') as f:
        json.dump(hits, f, indent=4)

    if f.closed:
        print("Finished updating " + product_list_filepath)
    else:
        print("file not closed")

if __name__ == '__main__':
    main()
