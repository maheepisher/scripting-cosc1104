"""
File Name: is_positive.py

Author: Maheep Isher Singh Chawla (100909435), Poorva Sharma (100934359)

Date: 4 Oct'2024

Description: This file defines a function is_positive which returns True if the number passed is positive number, otherwise returns False.


"""


def is_positive(number:float):
    if number > 0:
        return True
    else:
        return False
    
if __name__ == "__main__":
    print(is_positive(3.02))            # returns True
    print(is_positive(-1.3))           # returns False
    print(is_positive(-10))             # returns False
    print(is_positive(50))              # returns True