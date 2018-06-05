from random import randint

x = 6
y = 6
def cube ():
    n=1
    while True:
        x = randint (1, 6)
        y = randint (1, 6)
        if x + y == 8 :
            print (x, y, n)
            break
        n += 1
cube()