# Define your Fraction class here
class Fraction():

    def __init__(self, numerator, denominator):
        self.numerator = numerator
        self.denominator = denominator

    def get_numerator(self):
        return self.numerator

    def get_denominator(self):
        return self.denominator

    def set_numerator(self, new_numerator):
        self.numerator = new_numerator

    def set_denominator(self, new_denominator):
        if new_denominator == 0:
            print("Denominator cannot be 0")
        else:
            self.denominator = new_denominator

    def __str__(self):
        return str(self.numerator) + '/' + str(self.denominator)

    def add(self, other_fraction):
        self.numerator = self.numerator*other_fraction.denominator + other_fraction.numerator*self.denominator
        self.denominator = self.denominator*other_fraction.denominator
        # return numerator_sum + "/" + denominator_sum

    def subtract(self, other_fraction):
        self.numerator = (self.numerator*other_fraction.denominator - other_fraction.numerator*self.denominator)
        self.denominator = (self.denominator*other_fraction.denominator)
        # return numerator_diff + "/" + denominator

    def multiply(self, other_fraction):
        self.numerator = (self.numerator * other_fraction.numerator)
        self.denominator = (self.denominator * other_fraction.denominator)
        # return numerator_product + "/" + denominator_product

    # def __reduce__(self):
        # Fraction(numerator, denominator)


if __name__ == '__main__':
    # put your code that utilizes your Fraction class here
    fraction1 = Fraction(1, 2)
    fraction2 = Fraction(1, 4)

    print(fraction1, fraction2)
    print(fraction1.numerator, fraction1.denominator)
    print(fraction2.numerator, fraction2.denominator)
    fraction1.add(fraction2)
    print(fraction1)
    # print(fraction1.get_denominator())
    # print(fraction1.subtract(fraction2))
    # print(fraction1.multiply(fraction2))
    pass
