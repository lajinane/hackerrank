'''
https://www.hackerrank.com/challenges/polar-coordinates/problem

https://docs.python.org/2/library/cmath.html

Polar coordinates are an alternative way of representing Cartesian coordinates or Complex Numbers.

z = x + yj
z : complex number
x : real part
y : imaginary part
j : imaginary unit

A polar coordinate (r,p)
is completely determined by modulus « r » and phase angle « p »

To convert complex number « z » to its polar coordinate :
r = sqrt(x^2 + y^2)  distance from z to origin
p = counter clockwise angle measured from the positive x-axis to the line segment that joins « z »  to the origin.


To return the phase (argument) of a complex number. 
>>> cmath.phase(complex(-1.0, 0.0))
3.1415926535897931

To return the modulus (absolute value) of a complex number.
>>> abs(complex(-1.0, 0.0))
1.0

To convert to complex number
>>> complex(1+2j)
(1+2j)
'''

import cmath

z = complex(input())
# print(z.real, z.imag)

print(abs(z))
print(cmath.phase(z))

# OR

print(abs(z), cmath.phase(z), sep='\n')

# OR using cmath.polar

polar = cmath.polar(z)
print(f"{polar[0]}\n{polar[1]}")
