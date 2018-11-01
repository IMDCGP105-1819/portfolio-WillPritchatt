def fib(n):
    if n == 1 or n == 0:
        return n
    else:
        return fib(n-1) + fib(n-2)


sequence_location = int(input("What position in the Fibonacci do you want to find: "))
print(fib(sequence_location))
