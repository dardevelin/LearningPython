# For reduce
from functools import reduce

## Lambda
a = [1, 2, 3, 4]
print(a)
b = list(map(lambda x: x ** 2, a))
print(b)

c = list(map(lambda x, y: x + y, a, b))
print(c)


## Filters
                          ##condition
d = list(filter(lambda x: x % 2 == 0, b))
print(d)

## Reduce
e = reduce(lambda x,y: x+y, d)
print(e)