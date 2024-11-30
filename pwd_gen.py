import random, string

def genPass(min_len,digit,special):
    numbers = string.digits
    special_char = string.punctuation
    charaters = string.ascii_letters
    if digit:
        charaters += numbers
    if special:
        charaters += special_char
    pwd = []
    while True:
        for _ in range(min_len):
            pwd.append(random.choice(charaters))
        if digit:
            has_num = False
            for i in pwd:
                if i in numbers:
                    has_num = True
                    break
            if not has_num:
                pwd.pop()
                pwd.append(random.choice(numbers))
        random.shuffle(pwd)
        if special:
            has_special = False
            for i in pwd:
                if i in special_char:
                    has_special = True
                    break
            if not has_special:
                pwd.pop()
                pwd.append(random.choice(special_char))
        break
    random.shuffle(pwd)
    password = ''
    for i in pwd:
        password+=i
    return password

min_len = input('input the minimum length must be 3 or greater: ')
while True:
    if min_len.isdigit() and int(min_len)>=3:
        break
    else:
        print('invalid input length must be an +ve integer')
digit = input('do you want numbers in your password: ').lower() == 'y'
special = input('do you want special in your password: ').lower() == 'y'
pwd = genPass(int(min_len),digit,special)
print(pwd)

