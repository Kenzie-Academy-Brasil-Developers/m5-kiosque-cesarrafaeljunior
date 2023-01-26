from menu import products


def get_product_by_id(id):
    if type(id) != int:
        raise TypeError("product id must be an int")
    for product in products:
        if product["_id"] == id:
            return product


def get_products_by_type(type_product):
    if type(type_product) != str:
        raise TypeError("product type must be a str")
    products_filter = [product for product in products if product["type"] == type_product]
    return products_filter


def add_product(menu, *args):
    new_id = 0
    new_id = max([product["_id"] + 1 for product in menu if product["_id"] > new_id])
    for product in args:
        product["_id"] = new_id
        new_id += 1
        menu.append(product)
    return product


def menu_report():
    products_count = len(products)
    price = sum([product["price"] for product in products])
    average_price = round(price / products_count, 2)
    types_counts = {}

    for product in products:
        type_product = product["type"]
        if type_product in types_counts:
            types_counts[type_product] += 1
        else:
            types_counts[type_product] = 1

    common_type = max(types_counts, key=types_counts.get)

    report = {
        "Products Count": products_count,
        "Average Price": average_price,
        "Common Type": common_type
    }

    return report
