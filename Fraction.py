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
        return self.numerator + '/' + self.denominator

    def add(self, other_fraction):
        numerator_sum = str(int(self.numerator)*int(other_fraction.denominator) + int(other_fraction.numerator)*int(self.denominator))
        denominator_sum = str(int(self.denominator)*int(other_fraction.denominator) + int(other_fraction.denominator)*int(self.denominator))
        return numerator_sum + "/" + denominator_sum

    def subtract(self, other_fraction):
        numerator_diff = str(int(self.numerator)*int(other_fraction.denominator) - int(other_fraction.numerator)*int(self.denominator))
        denominator = str(int(self.denominator)*int(other_fraction.denominator))
        return numerator_diff + "/" + denominator

    def multiply(self, other_fraction):
        numerator_product = str(int(self.numerator) * int(other_fraction.numerator))
        denominator_product = str(int(self.denominator) * int(other_fraction.denominator))
        return numerator_product + "/" + denominator_product

    # def __reduce__(self):
        # Fraction(numerator, denominator)

def main():
    fraction1 = Fraction("2", "3")
    fraction2 = Fraction("3", "4")
    # print(fraction1)
    print(fraction1.add(fraction2))
    print(fraction1.subtract(fraction2))
    print(fraction1.multiply(fraction2))


main()
# if __name__ == '__main__':
#     # put your code that utilizes your Fraction class here
#     pass
