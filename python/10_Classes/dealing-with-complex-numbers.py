'''
https://www.hackerrank.com/challenges/class-1-dealing-with-complex-numbers/problem

complex number
a + bi

(a+bi) + (c+di) = (a+c)+(b+d)i

(a+bi) − (c+di) = (a−c)+(b−d)i

(a+bi) . (c+di) = (ac−bd)+(ad+bc)i

(a+bi) / (c+di) = (ac+bd / c^2+d^2) + (bc-ad / c^2+d^2)i

mod(a+bi) = sqrt(a^2 + b^2)

'''

import math


class Complex(object):
    def __init__(self, real, imaginary):
        self.re = real
        self.im = imaginary

    def __add__(self, no):
        return Complex(self.re + no.re, self.im+no.im)

    def __sub__(self, no):
        return Complex(self.re-no.re, self.im-no.im)

    def __mul__(self, no):
        return Complex(self.re*no.re - self.im*no.im,
                       self.re*no.im + self.im*no.re)

    def __truediv__(self, no):
        denominator = no.re**2 + no.im**2
        re_truediv = (self.re*no.re + self.im*no.im) / denominator
        im_truediv = (self.im*no.re - self.re*no.im) / denominator
        return Complex(re_truediv, im_truediv)

    def mod(self):
        return Complex(math.sqrt(self.re**2 + self.im**2), 0)

    def __str__(self):
        if self.im == 0:
            result = "%.2f+0.00i" % (self.re)
        elif self.re == 0:
            if self.im >= 0:
                result = "0.00+%.2fi" % (self.im)
            else:
                result = "0.00-%.2fi" % (abs(self.im))
        elif self.im > 0:
            result = "%.2f+%.2fi" % (self.re, self.im)
        else:
            result = "%.2f-%.2fi" % (self.re, abs(self.im))
        return result


if __name__ == '__main__':
    c = map(float, input().split())
    d = map(float, input().split())
    x = Complex(*c)
    y = Complex(*d)
    print(*map(str, [x+y, x-y, x*y, x/y, x.mod(), y.mod()]), sep='\n')
