'''
https://www.hackerrank.com/challenges/py-collections-ordereddict/problem
https://docs.python.org/3/library/collections.html#collections.OrderedDict

An OrderedDict is a dictionary that remembers the order of the keys that were inserted first. 
If a new entry overwrites an existing entry, the original insertion position is left unchanged.

Note : Default dict remembers the key insertion order since Python 3.7 

>>> ordinary_dictionary = {}
>>> ordinary_dictionary['a'] = 1
>>> ordinary_dictionary['b'] = 2
>>> ordinary_dictionary['c'] = 3
{'a': 1, 'c': 3, 'b': 2}

>>> ordered_dictionary = OrderedDict()
>>> ordered_dictionary['a'] = 1
>>> ordered_dictionary['b'] = 2
>>> ordered_dictionary['c'] = 3
OrderedDict([('a', 1), ('b', 2), ('c', 3)])

>>> s = "a,b,c,d"
>>> s.rsplit(',', 1)
['a,b,c', 'd']
>>> s.rsplit(',', 2)
['a,b', 'c', 'd']
>>> s.rpartition(',')
('a,b,c', ',', 'd')

rsplit() lets you specify how many times to split
rpartition() only splits once, returns (prefix, delimiter, postfix) and is faster for the single split case.

'''

from collections import OrderedDict

n = int(input())
d = OrderedDict()

for _ in range(n):
    name, price = input().rsplit(' ', 1)
    d[name] = int(price) + d.get(name, 0)

for k, v in d.items():
    print(k, v)
