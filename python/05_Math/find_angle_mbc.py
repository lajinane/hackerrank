'''
https://www.hackerrank.com/challenges/find-angle/problem

° = chr(176)
'''

import math

AB, BC = int(input()), int(input())

# hypotenuse AC
AC = math.sqrt(pow(AB, 2)+pow(BC, 2))

# half the hypotenuse AC = AM = MC
half_AC = AC / 2

# half BC
half_BC = BC / 2

# MBC angle
angle_MBC = round(math.degrees(math.acos(half_BC / half_AC)))

print(f'{angle_MBC}{chr(176)}')
