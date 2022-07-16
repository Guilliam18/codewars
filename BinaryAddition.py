# Name: Binary Addition
# https://www.codewars.com/kata/551f37452ff852b7bd000139
# Implement a function that adds two numbers together and returns their sum in binary. 

def add_binary(a,b):
    sum = a + b
    return bin(sum)[2:]