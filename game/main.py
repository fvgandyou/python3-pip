import random

def choose_option():
  options = ('scissors', 'paper', 'rock')
  user_option = input('Select rock, paper or scissors: ').lower()
  computer_option = random.choice(options)
  if not user_option in options:
    print('you chose a wrong option, try again')
    return None, None
  print(f'you chose {user_option} and the computer chose {computer_option}')
  return user_option, computer_option

def start_game(user_option, computer_option, user_wins, computer_wins):
  if user_option == computer_option:
    print('its a tie')
  elif user_option == 'scissors' and computer_option == 'paper' or user_option == 'paper' and computer_option == 'rock' or user_option == 'rock' and computer_option == 'scissors':
    user_wins += 1
    print(f'{user_option} beats {computer_option}, you won!')
  else:
    computer_wins += 1
    print(f'{computer_option} beats {user_option}, the computer won!')
  return user_wins, computer_wins

def total_winner(user_wins, computer_wins):
  if user_wins == 2:
    print('You winner, congratulations')
    exit()
  if computer_wins == 2:
    print('You loser, try again')
    exit()

def run_game():
  user_wins, computer_wins, rounds = 0, 0, 1
  while True:
    print('*' * 30)
    print(f'ROUND: {rounds}')
    print('*' * 30)
    user_option, computer_option = choose_option()
    if not user_option == None:
      user_wins, computer_wins = start_game(user_option, computer_option,
                                            user_wins, computer_wins)
      print(f'user wins: {user_wins} -- computer wins: {computer_wins}')
      rounds += 1
      total_winner(user_wins, computer_wins)
    else:
      continue

run_game()