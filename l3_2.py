def numb(a):
    if a >= 100 or a < -100:
        a = 0
        return a
    else:
        return a + 1

print(numb(80))