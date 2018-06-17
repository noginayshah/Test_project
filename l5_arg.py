# def func(first_num, second_num, c=3):
#     pass
#
# def func(*args):
#     for i in args:
#         print(i)
#     # return args
#
# print(func(1,3,3,4,56,7,8))
#
# def func(**kwargs):
#     return kwargs
#
# print(func(c=2, a=3, d=4))


# def func(*args, **kwargs):
#     return 'args= {} and kwargs= {}'.format(args, kwargs)
#
# print(func(1, 2, 4, 5, a=1, b=2))



def func(text):
    result_text = []
    for i in text:
        if i.isupper():
            result_text.append(i)
    my_string = ''.join(result_text)
    return my_string

print(func('Gjvkjvlk, Hjkjslkdjf, cjhvj ghjfhHJHGHJGHJjkhkhjkhk'))


import re

def secret_word(text):
    print(''.join(re.findall('[A-Z]', text)))

secret_word('Hello ffEll LLgfjg W')