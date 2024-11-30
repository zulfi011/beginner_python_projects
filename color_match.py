import random


def generate_colors(colors, length):
    gen_colors = []
    for i in range(length):
        gen_colors.append(random.choice(colors))
    return gen_colors


def code_guess(length, colors):
    while True:
        guess = input("Guess the code (space seperated) : ").upper()
        guessed = [x for x in guess if x != " "]
        condition = True
        if len(guessed) != length:
            condition = False
        for i in guessed:
            if i not in colors or len(i) != 1:
                condition = False
                break
        if condition:
            return guessed
        else:
            print('invalid input')


def chk_correct_pos(user, coded):
    correct_pos = 0
    for i in range(len(user)):
        if user[i] == coded[i]:
            user[i] = " "
            coded[i] = " "
            correct_pos += 1
    return correct_pos, [x for x in user
                         if x != " "], [x for x in coded if x != " "]


def chk_incorrect_pos(user, coded):
    incorrect_pos = 0
    for idx, val in enumerate(user):
        if val in coded:
            user[idx] = " "
            coded[coded.index(val)] = " "
            incorrect_pos += 1
    return incorrect_pos


def check_pos(user, coded):
    coded_copy = coded.copy()
    correct_pos, user, coded = chk_correct_pos(user, coded_copy)
    incorrect_pos = chk_incorrect_pos(user, coded_copy)
    coded_copy = coded
    return correct_pos, incorrect_pos


def game_start(colors, required_len, tries, coded_colors):
    while tries > 0:
        user_guess = code_guess(required_len, colors)
        if user_guess == coded_colors:
            print("\nyou won the coded colors were " + " ".join(coded_colors))
            break
        correct_pos, incorrect_pos = check_pos(user_guess, coded_colors)
        print(
            f"correct position : {correct_pos} | incorrect position : {incorrect_pos}"
        )
        tries -= 1
    else:
        print(
            f"\nyou are out of tries\nyou lost\nthe correct was {coded_colors}"
        )


def main():
    colors = ["R", "B", "G", "Y", "O", "W"]
    required_len = 4
    tries = 10
    coded_colors = generate_colors(colors, required_len)
    print("\nWelcome to matermind color match")
    print("Guess four digit code you have 10 tries....")
    print(f"Colors that make up the code are " + " ".join(colors) + "\n")

    game_start(colors, required_len, tries, coded_colors)


main()
