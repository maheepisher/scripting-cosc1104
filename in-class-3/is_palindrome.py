"""
File Name: is_palindrome.py

Author: Maheep Isher Singh Chawla (100909435), Poorva Sharma (100934359)

Date: 4 Oct'2024

Description: This file defines a function is_palindrome which which checks if passed string is a palindrome.


"""
def is_palindrome(string: str):
    i = 0
    j = len(string) - 1
    while(i <= j):
        if string[i] == string[j]:
            i += 1
            j = j - 1  
        else: 
            return False
        
    return True
    
if __name__ == "__main__":
    print(is_palindrome("racecar"))             # returns True
    print(is_palindrome("1223221"))             # returns True
    print(is_palindrome("12345678"))            # returns false
    print(is_palindrome("nitin"))               # returns True
    print(is_palindrome("maheep"))              # returns False
        
        
        
        