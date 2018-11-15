class Fraction:

    def __init__(self, num, denom):
        self.num = num
        self.denom = denom

    def addition(self, num2, denom2):
        numerator = (self.num * denom2) + (num2 * self.denom)
        denominator = self.denom * denom2
        return numerator, denominator

    def subtraction(self, num2, denom2):
        numerator = (self.num * denom2) - (num2 * self.denom)
        denominator = self.denom * denom2
        return numerator, denominator

    def multiply(self, num2, denom2):
        numerator = self.num * num2
        denominator = self.denom * denom2
        return numerator, denominator

    def divide(self, num2, denom2):
        numerator = self.num * denom2
        print(numerator)
        denominator = self.denom * num2
        return numerator, denominator

    def invert(self):
        return self.denom, self.num


fraction_1 = Fraction(7, 16)
fraction_2 = Fraction(9, 25)
add_fraction = fraction_1.addition(fraction_2.num, fraction_2.denom)
sub_fraction = fraction_1.subtraction(fraction_2.num, fraction_2.denom)
mult_fraction = fraction_1.multiply(fraction_2.num, fraction_2.denom)
div_fraction = fraction_1.divide(fraction_2.num, fraction_2.denom)
inv_fraction1 = fraction_1.invert()
inv_fraction2 = fraction_2.invert()

print("Added Fraction: {0}/{1}".format(add_fraction[0], add_fraction[1]))
print("Subtracted Fraction: {0}/{1}".format(sub_fraction[0], sub_fraction[1]))
print("Multiplied Fraction: {0}/{1}".format(mult_fraction[0], mult_fraction[1]))
print("Divided Fraction: {0}/{1}".format(div_fraction[0], div_fraction[1]))
print("Inverted Fractions: {0}/{1}, {2}/{3}".format(inv_fraction1[0], inv_fraction1[1], inv_fraction2[0], inv_fraction2[1]))
