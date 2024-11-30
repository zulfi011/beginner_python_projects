import random

data_dict = {
    "animal": ["lion", "cat", "elephant", "tiger", "giraffe"],
    "city": ["tokyo", "lahore", "paris", "sydney", "beijing"],
    "country": ["japan", "usa", "france", "australia", "china"],
    "name": ["alice", "bob", "eva", "david", "sophia"],
    "food": ["sushi", "pizza", "croissant", "burger", "noodles"]
}

def main():
    print('Hangman game!!!!')
    while True:
        play = input('do you want to play (y/n): ').lower()
        if play == 'y':
            break
        elif play =='n':
            quit()
        else:
            print('not a valid option')
    all_values = []
    for val in data_dict.values():
        for i in val:
            all_values.append(i)
    rand_val = random.choice(all_values)
    hint = ''
    for key,val in data_dict.items():
        if rand_val in val:
            hint = key
    print('hint: ',hint)
    tries = 5
    tracer = (len(rand_val)*'* ').split(' ')
    print(''.join(tracer))
    while tries>0:
        guess = input('guess : ').lower()
        if guess in tracer:
            print('already guessed')
            continue
        elif guess in rand_val:
            for idx,val in enumerate(rand_val):
                if guess == val:
                    tracer[idx] = val
            print(''.join(tracer))
        else:
            tries -= 1
            print('wrong guess ')
            print(''.join(tracer))
            print('tries left ',tries)
        if '*' in tracer:
            continue
        else:
            print('you won')
            quit()
    print('you lost man has been hanged')
    print('answer was ',rand_val)

if __name__=="__main__":
    main()