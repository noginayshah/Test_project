def func1(pro='znak'):
    return pro.upper() + '!!!'
def func2(word='zero'):
    return word.lower() + 'Afdsfs'
def db_before(func):
    print('Deystviya do vuzova fynkcii')
    print(func())
    print('Deistviya posle vuzova fyncii')
db_before(func1)
print('?' * 100)
db_before(func2)

