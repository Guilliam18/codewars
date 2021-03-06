# Name: Create Phone Number
# https://www.codewars.com/kata/525f50e3b73515a6db000b83
# Write a function that accepts an array of 10 integers (between 0 and 9), 
# that returns a string of those numbers in the form of a phone number.

def create_phone_number(n):
    return "(" + ''.join(str(e) for e in n[0:3]) + ") " + ''.join(str(e) for e in n[3:6]) + "-" + ''.join(str(e) for e in n[6:10])