from menu import products


def get_product_by_id(id):
    for product in products:
        if product["_id"] == id:
            return product


def get_products_by_type(type):
    array = []
    for product in products:
        if product["type"] == type:
            array.append(product)
    return array
