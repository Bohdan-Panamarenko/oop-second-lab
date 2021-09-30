class Rectangle:
    def __init__(self, width: float = 1, height: float = 1):
        if width < 0 or width > 20:
            raise ValueError("width can not be less than 0 or more than 20")
        self._width = width

        if height < 0 or height > 20:
            raise ValueError("height can not be less than 0 or more than 20")
        self._height = height

    def area(self):
        return self._width * self._height

    def perimeter(self):
        return 2 * (self._width + self._height)

    def set_width(self, width: float):
        if width < 0 or width > 20:
            raise ValueError("width can not be less than 0 or more than 20")

        self._width = width

    def set_height(self, height: float):
        if height < 0 or height > 20:
            raise ValueError("height can not be less than 0 or more than 20")

        self._height = height

    def get_width(self):
        return self._width

    def get_height(self):
        return self._height


try :
    rect = Rectangle(10, 4.5)
    print(f"Rectangle: {rect.get_height()} {rect.get_width()}")
    print(rect.area())
    print(rect.set_height(-1))
except ValueError as err:
    print(err)
