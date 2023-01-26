from management.product_handler import get_product_by_id


def calculate_tab(account):
    products_consumed = []
    for i, product in enumerate(account):
        product_consumed = get_product_by_id(product["_id"])
        product_consumed["amount"] = account[i]["amount"]
        products_consumed.append(product_consumed)
    prices = 0
    for product in products_consumed:
        price = product["price"]
        amount = product["amount"]
        prices += price * amount
    subtotal = {

        "subtotal": f"${round(prices, 2)}"

    }
    return subtotal
