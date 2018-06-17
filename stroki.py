#stroka1 = 'privet' + 'hello'

#for i in stroka1:
 #   print(i)

#srez = 'Python'
#print(srez[0] == 'P')
#print(srez[0])

# srez = 'Python'
# c = srez[0:2] + srez[1:3]
# print(c)
# print(srez[0] == 'P')
# print(srez[0])

# srez = '<sitemap><url>'
# print(srez.split('<')
# print(srez.startswith('<sitem'))


def count_char(stoka1, stroka2):
    t = 0
    for i in stoka1:
        if i == stroka2:
            t += 1
    print(t)

count_char('Hello world', 'o')
