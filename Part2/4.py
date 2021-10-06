from typing import  List

class BinaryTree:
    """
    This class describes binary tree of products.
    Single node contains code and price of product.
    """
    def __init__(self, code: int, price: float):
        self._check_code_price(code, price)

        self.code = code
        self.price = price
        self.left: BinaryTree = None
        self.right: BinaryTree = None

    def _check_code_price(self, code: int, price: float = 0):
        if code < 0:
            raise ValueError("Code can not be less than 0")

        if price < 0:
            raise ValueError("Price can not be less than 0")

    def add(self, code: int, price: float):
        if code < self.code:
            if self.left is not None:
                self.left.add(code, price)
            else:
                self.left = BinaryTree(code, price)
        else:
            if self.right is not None:
                self.right.add(code, price)
            else:
                self.right = BinaryTree(code, price)

    def list(self, list: List[str] = []):
        if self.left is not None:
            self.left.list()

        list.append(f"{self.code}: {self.price}")

        if self.right is not None:
            self.right.list()

        return list

    def find(self, code: int):
        currNode = self

        while True:
            if currNode is None or currNode.code == code:
                break
            elif code < currNode.code:
                currNode = currNode.left
            else:
                currNode = currNode.right

        return currNode

    def cost_of_product(self, code: int, num_of_products: int):
        self._check_code_price(code)

        if num_of_products < 0:
            raise ValueError("Number of products can not be less than 0")

        product = self.find(code)
        if product is None:
            raise ValueError(f"There is no product with code {code}")

        return product.price * num_of_products


products = { 1: 1.99, 2: 10.99, 3: 6.75, 4: 1.75, 5: 5.25, 5: 6.99, 6: 7.99 }
tree = BinaryTree(0, 4.99)

for key in products:
    tree.add(key, products[key])

print(tree.list())

print(tree.cost_of_product(2, 10))

# print(tree.cost_of_product(7, 4))