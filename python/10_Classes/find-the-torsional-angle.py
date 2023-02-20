'''
https://www.hackerrank.com/challenges/class-2-find-the-torsional-angle/problem

P1 = (x1,y2,z3)
P2 = (x2,y2,z3)

subtract
P1-P2 = (x1 - x2, y1 - y2, z1 - z2)

dot product 
P1.P2 = (x1 * x2) + (y1 * y2) + (z1 * z2) = ...

cross product
P1xP2 = ( y1 * z2 - z1 * y2,
          z1 * x2 - x1 * z2,
          x1 * y2 - y1 * x2 )

absolute
|P| = (x^2 + y^2 + z^2) ^ 0.5

Points a, b, c, d
Torsional Angle between a,b,c and b,c,d
X = (b - a) x (c - b)
y = (c - b) x (d - c)
D = ( X.Y ) / ( |X| * |Y| )
angle = cos(D)

'''

import math


class Points(object):
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __sub__(self, no):
        return Points(self.x - no.x,
                      self.y - no.y,
                      self.z - no.z)

    def dot(self, no):
        return (self.x*no.x) + (self.y*no.y) + (self.z*no.z)

    def cross(self, no):
        return Points(self.y * no.z - self.z * no.y,
                      self.z * no.x - self.x * no.z,
                      self.x * no.y - self.y * no.x)

    def absolute(self):
        return pow((self.x ** 2 + self.y ** 2 + self.z ** 2), 0.5)


if __name__ == '__main__':
    points = list()
    for i in range(4):
        a = list(map(float, input().split()))
        points.append(a)

    a, b, c, d = Points(*points[0]), Points(*points[1]
                                            ), Points(*points[2]), Points(*points[3])
    x = (b - a).cross(c - b)
    y = (c - b).cross(d - c)
    angle = math.acos(x.dot(y) / (x.absolute() * y.absolute()))

    print("%.2f" % math.degrees(angle))
