#!/usr/bin/python3
def fizzbuzz():
    for i in range(1, 101):
        if (i % 3 == 0 or (i / 10) + (i % 10) == 3):
            if (i % 5 == 0 or ((i % 10) == 0 or (i % 10) == 5)):
                print("FizzBuzz", end=" ")
            else:
                print("Fizz", end=" ")
        elif (i % 5 == 0 or ((i % 10) == 0 or (i % 10) == 5)):
            print("Buzz", end=" ")
        elif (i == 1):
            print("{:d}".format(i), end=" ")
        else:
            print("{:d}".format(i), end=" ")
