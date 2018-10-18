low = int(input("Enter the lowest value: "))
high = int(input("Enter the highest value: "))

for i in range(low, high + 1):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)
