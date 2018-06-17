# print(not False and not None or 0 or [])

# from random import randint
#
# def lotereya():
#     numbers = [
#         1, 2, 3, 4, 5, 6, 7, 8, 9, 10,
#         11, 12, 13, 14, 15, 16, 17, 18, 19, 20,
#         21, 22, 23, 24, 25, 26, 27, 28, 29, 30,
#         31, 32, 33, 34, 35, 36, 37, 38, 39, 40,
#         41, 42, 43, 44, 45, 46, 47, 48, 49, 50,
#         51, 52
#     ]
#
#     for a in range(1, 6):
#         n = randint(1, 52)
#         numbers.pop(n)
#
#         return
#
# lotereya()
# print(lotereya())

import random

def lottery(num_win_balls, total_balls):
    result_list = []
    if num_win_balls <= total_balls:
        balls = list(range(1, total_balls + 1))
        for i in range(num_win_balls):
            random.shuffle(balls)
            result_list.append(balls.pop())
            result_list.sort()
        return result_list
    else:
        return 'No'

print(lottery(6, 100))