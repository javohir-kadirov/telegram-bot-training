import json


product_json = '''
{
    "id": 101,
    "name": "Gaming Mouse",
    "price": 180000,
    "available": true,
    "tags": ["gaming", "electronics"]
}
'''


def process_product(product_attributes: str) -> dict:
    product = json.loads(product_attributes)
    product["discount"] = 10
    print(product["name"])
    print(product["price"])
    
    if product["available"]:
        print("Product is available")
    else:
        print("Product is unavailable")

    return product


result = json.dumps(process_product(product_json))
print(result)
    