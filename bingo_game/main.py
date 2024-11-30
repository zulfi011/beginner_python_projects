from card import createCard
import random

def checkVertically(card):
    all_values = []
    for i in range(len(card)):
        new_val = []
        for val in card.values():
            new_val.append(val[i])
        all_values.append(new_val)
    for i in all_values:
        if sum(i)==0:
            return True

def checkHorizontally(card):
    for val in card.values():
        if sum(val)==0:
            return True

def checkDiagonally(card):
    all_values = []
    for val in card.values():
        for i in val:
            all_values.append(i)
    num_lft = 0
    num_rt = 4
    lft_to_rt = []
    rt_to_lft = []
    for i in range(len(card)):
        lft_to_rt.append(all_values[num_lft])
        rt_to_lft.append(all_values[num_rt])
        num_lft += 6
        num_rt += 4
    if sum(lft_to_rt)==0 or sum(rt_to_lft)==0:
        return True

def checkCards(card):
    if checkHorizontally(card) or checkVertically(card) or checkDiagonally(card):
        return True

def main():
    players_amt = 0
    while True:
        line = input('input the amount of players or q to quit: ').lower()
        if line == 'q':
            quit()
        elif line.isdigit():
            players_amt = int(line)
            break
        else:
            print('not a valid input')
    player_cards = []
    for i in range(players_amt):
        player_cards.append(createCard())
    for idx,ele in enumerate(player_cards):
        print(f'player {idx+1} cards: ')
        for key,val in ele.items():
            print(key,' ',val)
        print()
    rand_tracking = []
    while True:
        get_num = input('press any key to get number ')==""
        gen_num = 0
        if get_num:
            while True:
                random_num = random.randint(1,75)
                if random_num in rand_tracking:
                    continue
                rand_tracking.append(random_num)
                gen_num = random_num
                break
        print(f"number : {gen_num}")
        for i in player_cards:
            for val in i.values():
                for j in val:
                    if j == gen_num:
                        val[val.index(j)] = 0
        for idx,ele in enumerate(player_cards):
            print(f'player {idx+1} cards: ')
            for key,val in ele.items():
                print(key,' ',val)
            print()
        game_end = False
        for idx,ele in enumerate(player_cards):
            result = checkCards(ele)
            if result:
                print(f'bingo {idx+1} is the winner')
                game_end = True
                break
        if game_end:
            break

if __name__=="__main__":
    main()