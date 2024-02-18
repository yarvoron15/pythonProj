# import random
# win_nums = [1,2,3,4,5,6,7,8,9,10]
#
# def rand_num(win_nums):
#     return random.choice(win_nums)
#
# while True:
#     bank = 1000
#     win_num = rand_num(win_nums)
#     bid = int(input("Enter your bid (in dollars): "))
#     players_num = int(input(f"choose a number from 1 to 10: "))
#     if players_num == win_num:
#         bid *= 2
#         bank += bid
from game import casino_game

if __name__ == "__main__":
    casino_game()

