import random

WINNING_SCORE = 50


def roll_dice():
  LOW = 1
  HIGH = 6
  return random.randint(LOW, HIGH)


def players():
  while True:
    line = input('number of players 2-4: ')
    if line.isdigit():
      if 2 <= int(line) <= 4:
        return [0 for _ in range(int(line))]
      else:
        print('must be between 2 - 4')
    else:
      print('must be an integer')


def main():
  players_score = players()
  while max(players_score) < WINNING_SCORE:
    for i in range(len(players_score)):
      print(f"player {i+1} turn")
      print(f"your main score is {players_score[i]}")
      current = 0
      while True:
        roll = input('do you want to roll (y)')
        if roll != "y":
          print('your turn is over')
          break
        else:
          value = roll_dice()
          if value == 1:
            current = 0
            print('you rolled 1 turn over')
            break
          else:
            print('you rolled: ', value)
            current += value
            print(f"your current score : {current}")
      players_score[i] += current
      print(f"your total score : {players_score[i]}\n")
      if players_score[i] >= WINNING_SCORE:
        print(f'player {i+1} is the winner')
        break


if __name__ == "__main__":
  main()
