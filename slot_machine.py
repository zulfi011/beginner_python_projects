import random

symbol_value = {
    "A" : 5,
    "B" : 4,
    "C" : 3,
    "D" : 2
    }

MAX_LINES = 3
ROWS = 3
COLUMNS = 3

def line_checker(ch):
    ele = ch[0]
    for item in ch:
        if item != ele:
            return 0
    return ele

def winnings(slots, lines, values, bet):
    win_amt = 0
    check_lst = []
    for slot in slots:
        check_lst.append(line_checker(slot))
    true_lines = len(check_lst)-check_lst.count(0)        
    for i in check_lst:
        if i != 0:
            if true_lines > lines:
                win_amt += values[i]*lines*bet
            elif true_lines <= lines:
                win_amt += values[i]*true_lines*bet

    return win_amt

def print_slot_machine(slots):
    for slot in slots:
        for idx,val in enumerate(slot):
            if 0<=idx<=1:
                print(val, end=" | ")
            else:
                print(val)

def get_slot_machine_spin(symbols, row, column):
    all_symbols = []
    for symbol in symbols.keys():
        all_symbols.append(symbol)
    columns = []
    for _ in range(column):
        column = []
        used_val = all_symbols[:]
        for _ in range(row):
            value = random.choice(used_val)
            column.append(value)
            used_val.remove(value)
        columns.append(column)
    rows = []
    count = 0
    for _ in range(row):
        row = []
        for i in columns:
            row.append(i[count])
        rows.append(row)
        count += 1
    return rows

def get_bet_per_line():
    bet_per_line = 0
    while True:
        line = input('how much to bet on each line: $')
        if line.isdigit():
            bet_per_line = int(line)
            break
        else:
            continue
    return bet_per_line

def get_num_of_lines():
    bet_line = 0
    while True:
        line = input('how many lines to bet 1-3: ')
        if line.isdigit():
            if 1<=int(line)<=MAX_LINES:
                bet_line = int(line)
                break
            else:
                print('must be between 1-3')
        else:
            print('must be an integer')
    return bet_line

def deposit():
    deposit_amt = 0
    while True:
        line = input('deposit amount: $')
        if line.isdigit():
            deposit_amt = int(line)
            break
        else:
            print('must be an integer')
    return deposit_amt

def spin(balance):
    lines = get_num_of_lines()
    while True:
        bet = get_bet_per_line()
        total_bet = bet * lines
        if total_bet > balance:
            print(
                f"You do not have enough to bet that amount, your current balance is: ${balance}")
        else:
            break
    print(f"You are betting ${bet} on {lines} lines. Total bet is equal to: ${total_bet}")
    slots = get_slot_machine_spin(symbol_value,ROWS,COLUMNS)
    input('press enter to roll slot machine!!!')
    print_slot_machine(slots)
    winning_amt = winnings(slots, lines, symbol_value, bet)
    print(f"you won : ${winning_amt}")
    return winning_amt - total_bet

def main():
    current_balance = 0
    while True:
        deposit_amt = deposit()
        current_balance += deposit_amt
        print(f"your current balance is: ${current_balance}")
        play = input('press enter to play and q to quit! ').lower()
        if play=="q":
            print(f"you are going out with: ${current_balance}")
            break
        current_balance += spin(current_balance)
        print(f"your current balance is: ${current_balance}")
        again = input('press enter to play again and w to widthdraw: ').lower()
        if again=="w":
            print(f"you are going out with amount: ${current_balance}")
            break
        else:
            continue

if __name__=="__main__":
    main()