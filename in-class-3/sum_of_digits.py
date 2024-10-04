"""
File Name: sum_of_digits.py

Author: Maheep Isher Singh Chawla (100909435), Poorva Sharma (100934359)

Date: 4 Oct'2024

Description: This file defines a function sum_of_digits which returns sum of all the digits of that number.


"""

def sum_of_digits(number: int):
    digits_sum = 0
    str_number = str(number)
    for i in range(0, len(str_number)):
        digits_sum += int(str_number[i])
    
    return digits_sum

if __name__ == "__main__":
    print(sum_of_digits(31))            # returns 4
    print(sum_of_digits(23))           # returns 5
    print(sum_of_digits(21))             # returns 3
    print(sum_of_digits(111))              # returns 3