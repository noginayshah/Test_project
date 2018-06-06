import random

def move_roulette(num):
    val = random.randint(1, 36)
    return val == num

total_money = 100
win = 0
loss = 0
for p in range(50):
    bet = 1
    step = move_roulette(10)
    if step is True:
        total_money += 35 * bet
        win += 1
    else:
        total_money -= bet
        loss += 1

print("Win", win, "Loss", loss, "Money", total_money)