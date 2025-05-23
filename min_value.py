#!/usr/bin/env python3
# Created by: Gustav I
# Created on: April 19, 2025
# This program generates 10 random numbers and finds
# the min value with a for..in loop

# Constants
MAX_ARRAY_SIZE = 10
MIN_NUM = 0
MAX_NUM = 100

import random


# Function to find the minimum value using a for..in loop
def find_min_value(numbers):
    min_value = numbers[0]
    for num in numbers:
        if num < min_value:
            min_value = num
    return min_value


# Main Program
def main():
    random_numbers = []

    # Generate random numbers
    for i in range(MAX_ARRAY_SIZE):
        number = random.randint(MIN_NUM, MAX_NUM)
        random_numbers.append(number)

    # Display generated numbers
    print("Random numbers:", random_numbers)

    # Find and display the minimum value
    min_value = find_min_value(random_numbers)
    print("Minimum value:", min_value)


# Run the program
if __name__ == "__main__":
    main()
