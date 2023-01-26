from menu import products


def get_product_by_id(id):

    if type(id) != int:
        raise TypeError("product id must be an int")

    found_id = [product for product in products if product["_id"] == id]

    if found_id:
        product, = found_id
        return product
    else:
        return {}


def get_products_by_type(type_product):
    if type(type_product) != str:
        raise TypeError("product type must be a str")

    found_product_by_type = [product for product in products if product["type"] == type_product]

    if found_product_by_type:
        return found_product_by_type
    else:
        return []


def add_product(menu, **kwargs):
    if menu != []:
        max_id = max([product["_id"] for product in menu])

        new_product = {
            "_id": max_id + 1,
            **kwargs
        }
        menu.append(new_product)
        return new_product
    else:
        new_product = {
            "_id": 1,
            **kwargs
        }
        menu.append(new_product)
        return new_product


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

    report = f"Products Count: {products_count} - Average Price: ${average_price} - Most Common Type: {common_type}"

    return report
