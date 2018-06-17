def number(z):
    if -10 < z < 10:
        return z + 5
    else:
        return z - 10

assert  number(10) == 0, u'wtf'
print(number(10))
