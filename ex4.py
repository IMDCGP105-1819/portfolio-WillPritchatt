my_name = "Will Pritchatt"
my_age = 19  # Yes, really!
my_height = 70  # Inches
my_weight = 187  # Pounds
my_eyes = "Blue"
my_hair = "Brown"
is_heavy = my_weight > 3000

# Constant to convert pounds into kilos
POUNDS_TO_KILO = 0.45359237
# Constant to convert inches into centimeters
INCHES_TO_CM = 0.39370

my_weight_kilo = round(my_weight * POUNDS_TO_KILO, 2)
my_height_cm = round(my_height / INCHES_TO_CM, 2)

print("Let's talk about {}.".format(my_name))
print("He is {} inches or {} centimeters tall.".format(my_height, my_height_cm))
print("He is {} pounds or {} kilos heavy.".format(my_weight, my_weight_kilo))
print("It is {} that he is overweight.".format(is_heavy))
print("He's got {} eyes and {} hair.".format(my_eyes, my_hair))

total = my_age + my_height + my_weight
print("If I add {}, {}, and {} together I get {}".format(my_age, my_height, my_weight, total))
