# Allows user to input their details. Details are assigned to corresponding variables
name = input("Please enter your name: ")
# int(input()) requires the user to input an integer value or the program will not work
age = int(input("Please enter your age: "))
height = int(input("Please enter your height in inches: "))
weight = int(input("Please enter your weight in pounds: "))
eyes = input("Please enter your eye colour: ")
hair = input("Please enter your hair colour: ")
is_heavy = weight > 3000


# Constant to convert pounds into kilos
POUNDS_TO_KILO = 0.45359237
# Constant to convert inches into centimeters
INCHES_TO_CM = 0.39370

my_weight_kilo = round(weight * POUNDS_TO_KILO, 2)
my_height_cm = round(height / INCHES_TO_CM, 2)

print("Let's talk about {}.".format(name))
print("He is {} inches or {} centimeters tall.".format(height, my_height_cm))
print("He is {} pounds or {} kilos heavy.".format(weight, my_weight_kilo))
print("It is {} that he is overweight.".format(is_heavy))
print("He's got {} eyes and {} hair.".format(eyes, hair))
