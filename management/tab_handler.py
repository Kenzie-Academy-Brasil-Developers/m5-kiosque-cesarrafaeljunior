from management.product_handler import get_product_by_id


def calculate_tab(account):
    products_consumed = []
    for i, product in enumerate(account):
        product_consumed = get_product_by_id(product["_id"])
        product_consumed["amount"] = account[i]["amount"]
        products_consumed.append(product_consumed)
    prices = sum([product["price"] * product["amount"] for product in products_consumed])
    subtotal = {

        "subtotal": f"${round(prices, 2)}"

    }
    return subtotal
