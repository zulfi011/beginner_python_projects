import random

def createCard():
    upper_limit = 1
    lower_limit = 15
    card = {}
    for i in ['B','I','N','G','O']:
        num = []
        while len(num)<5:
            rand_num = random.randint(upper_limit,lower_limit)
            if rand_num in num:
                continue
            num.append(rand_num)
        card.update({i:sorted(num)})
        upper_limit += 15
        lower_limit += 15
    return card


def main():
    result = createCard()
    for key,val in result.items():
        print(key,' ',val)

if __name__=="__main__":
    main()