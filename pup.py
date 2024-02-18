import random


def check_win(selected_slot, winning_slot):
    return selected_slot == winning_slot

def calculate_reward(bet_amount, is_win):
    if is_win:
        return bet_amount * 2
    else:
        return -bet_amount