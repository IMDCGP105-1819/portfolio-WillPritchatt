# cars is assigned the integer value 100
cars = 100
# space_in_a_car is assigned a floating point value of 4.0
space_in_a_car = 4.0
# drivers is assigned the integer value 30
drivers = 30
# passengers is assigned the integer value 90
passengers = 90
# cars_not_driven_ is defined by subtracting drivers from cars
cars_not_driven = cars - drivers
# cars_driven is a copy of drivers. It does not need to be used, drivers can be used in its place with no issues.
cars_driven = drivers
# carpool_capacity is defined by multiplying the cars driven by the spaces in the car
carpool_capacity = cars_driven * space_in_a_car
# average_passengers_per_car is calculated by dividing the number of passengers by the number of drivers
average_passengers_per_car = passengers / cars_driven

print("There are", cars, "cars available.")
print("There are only", drivers, "drivers available.")
print("There will be", cars_not_driven, "empty cars today.")
print("We can transport", carpool_capacity, "people today.")
print("We have", passengers, "to carpool today.")
print("We need to put about", average_passengers_per_car, "in each car.")
