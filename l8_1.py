# while True:
#     try:
#         x = int(input('Enter number: '))
#         # x = x / 0
#         # break
#     except (ValueError, NameError, TypeError) as err:
#         print('Number fail {}'.format(err))
#     else:
#         print('ne to')
#         # break
#     finally:
#         print('vsegda print')


# class MyException(Exception):
#     pass
# raise MyException()

# def shout(word='yes'):
#     return word.upper() + '!!!'
# scream = shout
# print(scream())
#
# del shout
# try:
#     print(shout())
# except NameError as qw:
#     print(qw)
# print(scream())

def shall():
    def whisper(word='yes'):
        return word.lower() + '...'



    print(whisper())
shall()
try:
    print(whisper())
except NameError as err:
    print(err)