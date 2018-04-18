class Fraction:

    def __init__(self, numerator, denominator):
        self.top = numerator
        self.bottom = denominator

    def __eq__(self, other):
        print(other)
        first_num = self.top * other.bottom
        second_num = other.top * self.bottom
        return first_num == second_num

    def __repr__(self):
        return "{0}/{1}".format(self.top, self.bottom)

    def __add__(self, other):
        other.top = self.top * other.bottom + other.top * self.bottom
        other.bottom = self.bottom * other.bottom
        a = other.top
        b = other.bottom
        while b:
            a, b = b, a % b
        other.top = other.top / a
        other.bottom = other.bottom / a
        return other


fr = Fraction(2, 9)
xx = Fraction(2, 3)

print(fr + xx)