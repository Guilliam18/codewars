# Name: Find the next perfect square! 
# 
# Description: Complete the findNextSquare method that finds the next integral perfect square after the one passed as a parameter. 
# Recall that an integral perfect square is an integer n such that sqrt(n) is also an integer.
# If the parameter is itself not a perfect square then -1 should be returned. You may assume the parameter is non-negative.
# 
# https://www.codewars.com/kata/56269eb78ad2e4ced1000013

import math
def find_next_square(sq):
    root = math.sqrt(sq)
    if root % 1 != 0:
        return -1
    return (root + 1)**2