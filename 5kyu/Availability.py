# Name: Pete, the baker
# https://www.codewars.com/kata/525c65e51bf619685c000059
# Write a function cakes(), which takes the recipe (object) and the available ingredients 
# (also an object) and returns the maximum number of cakes Pete can bake (integer).

import math
def cakes(recipe, available):
    total = 1000000
    for x in recipe:
        print(x)
        if x not in available:
            return 0
        temp = math.floor(available[x] / recipe[x])
        if temp < total:
            total = temp
    return total