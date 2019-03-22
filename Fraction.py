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
        self.__reduce__()
        return str(int(self.numerator)) + '/' + str(int(self.denominator))

    def add(self, other_fraction):
        self.numerator = self.numerator*other_fraction.denominator + other_fraction.numerator*self.denominator
        self.denominator = self.denominator*other_fraction.denominator

    def subtract(self, other_fraction):
        self.numerator = self.numerator*other_fraction.denominator - other_fraction.numerator*self.denominator
        self.denominator = self.denominator*other_fraction.denominator

    def multiply(self, other_fraction):
        self.numerator = self.numerator * other_fraction.numerator
        self.denominator = self.denominator * other_fraction.denominator

    def __reduce__(self):
        a = self.numerator
        b = self.denominator

        # Checks to see which out of the numerator and denominator is lower and finds to biggest common factor to divide
        if abs(a) <= b:
            while a > 1:
                if self.numerator % a == 0 and self.denominator % a == 0:
                    self.numerator /= a
                    self.denominator /= a
                    break
                else:
                    a -= 1
        else:
            while b > 1:
                if self.numerator % b == 0 and self.denominator % b == 0:
                    self.numerator /= b
                    self.denominator /= b
                    break
                else:
                    b -= 1


if __name__ == '__main__':
    # put your code that utilizes your Fraction class here
    print("** Fraction 1 **")
    user_numerator1 = int(input("Enter the numerator: "))
    user_denominator1 = int(input("Enter the denominator: "))
    fraction1 = Fraction(user_numerator1, user_denominator1)

    print("** Fraction 2 **")
    user_numerator2 = int(input("Enter the numerator: "))
    user_denominator2 = int(input("Enter the denominator: "))
    fraction2 = Fraction(user_numerator2, user_denominator2)

    display_fraction1 = fraction1
    display_fraction2 = fraction2

    for i in range(3):
        fraction1 = Fraction(user_numerator1, user_denominator1)
        fraction2 = Fraction(user_numerator2, user_denominator2)
        if i == 0:
            fraction1.add(fraction2)
            print(display_fraction1, "+", display_fraction2, "=", fraction1)
        elif i == 1:
            fraction1.subtract(fraction2)
            print(display_fraction1, "-", display_fraction2, "=", fraction1)
        else:
            fraction1.multiply(fraction2)
            print(display_fraction1, "*", display_fraction2, "=", fraction1)
    pass
