def list_of_numbers(lst1):
    n = 0
    for i in lst1:
        if i > 0:
            n += 1
    return 'кол-во полож чисел = {}'.format(n)

lst2 = [-10, -4, 2, -2, 4]
print(list_of_numbers(lst2))