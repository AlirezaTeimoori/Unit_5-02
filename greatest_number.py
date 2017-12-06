# Created by: Alireza Teimoori
# Created on: Nov 2017
# Unit_5-02
# makes a 10 number array and finds max

from numpy import random


def find_max_value(array = []):
    # finds max value in array
    
    max_number = array[0]
    
    for single_number in array:
        if max_number < single_number:
            max_number = single_number
            
    return max_number

# input
counter = 0
random_numbers = []

while counter < 10:

    single_number = random.randint(1, 10 + 1)

    print(single_number)

    random_numbers.append(single_number)

    counter = counter + 1

# process
largest_value = find_max_value(random_numbers)

# output
print("\nThe maximum value of the array is " + str(largest_value) + ".\n")
