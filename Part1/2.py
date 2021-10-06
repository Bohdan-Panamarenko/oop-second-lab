class Rational:
    def __init__(self, numerator: int = 1, denominator: int = 1):
        biggest_dem = self._biggest_denominator(numerator, denominator)
        if biggest_dem != 0:
            numerator /= biggest_dem
            denominator /= biggest_dem

        self._numerator = int(numerator)
        self._denominator = int(denominator)

    def __str__(self):
        return f"{self._numerator}/{self._denominator}"

    def fraction(self):
        return self._numerator / self._denominator

    def _biggest_denominator(self, a: int, b: int):
        while a != 0 and b != 0:
            if a > b:
                a = a % b
            else:
                b = b % a

        return a + b


r = Rational(2, 8)

print(r)
print(r.fraction())


