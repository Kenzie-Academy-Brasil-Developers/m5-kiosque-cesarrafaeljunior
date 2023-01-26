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


def add_product(menu, *args):
    new_id = 0
    new_id = max([product["_id"] + 1 for product in menu if product["_id"] > new_id])
    for product in args:
        product["_id"] = new_id
        new_id += 1
        menu.append(product)
    return product
