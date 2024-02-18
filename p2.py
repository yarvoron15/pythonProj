from pup import check_win, calculate_reward
import configparser
import random

config = configparser.ConfigParser()
config.read('settings.ini')
MY_MONEY = int(config['DEFAULT']['MY_MONEY'])

slots = list(range(1, 11))

def casino_game():
    global MY_MONEY
    while True:
        print(f"Your current balance: ${MY_MONEY}")
        selected_slot = int(input("Choose a slot (1-10): "))
        bet_amount = int(input("Enter your bet amount: $"))

        if bet_amount > MY_MONEY:
            print("Not enough funds. Game over.")
            break

        winning_slot = random.choice(slots)

        if check_win(selected_slot, winning_slot):
            reward = calculate_reward(bet_amount, True)
            MY_MONEY += reward
            print(f"Congratulations! You won ${reward}.")
        else:
            reward = calculate_reward(bet_amount, False)
            MY_MONEY += reward
            print(f"Sorry, you lost ${-reward}.")

        play_again = input("Do you want to play again? (y/n): ")
        if play_again.lower() != 'y':
            break

    print(f"Game over. Your final balance: ${MY_MONEY}")

if __name__ == "__main__":
    casino_game()