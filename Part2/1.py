from typing import Dict, List

class Product:
    """
    Single Product instance contains price, description and size of product.
    Size is a dict with str as key and int as value
    """
    def __init__(self, price: float, description: str, size: Dict[str, int]):
        self.price = price
        self.description = description
        self.size = size


class Customer:
    """
    Single Customer instance contains name, surname, patronumic and mobile phone of customer
    """
    def __init__(self, surname: str, name: str, patronymic: str, mobile_phone: str):
        self.surname = surname
        self.name = name
        self.patronymic = patronymic
        self.mobile_phone = mobile_phone


class Order:
    """
    Single Order instance contains list of Product instance, Customer instance, and name of currier
    """
    def __init__(self, products: List[Product], customer: Customer, who_carried: str):
        self.products = products
        self.customer = customer
        self.who_carried = who_carried

    def calc(self):
        summ = 0
        for product in self.products:
            summ += product.price

        return summ


order = Order(
    [
        Product(25, "Phone", {"width": 10, "height": 100, "length": 200}),
        Product(41, "Milk", {"width": 25, "height": 20, "length": 30})
    ],
    Customer("Panamarenko", "Bohdan", "Serhiiovish", "0660302346"),
    "Egor"
)

print(order.calc())
