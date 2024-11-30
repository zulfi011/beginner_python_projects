from cryptography.fernet import Fernet

def gen_key():
    """Making sure key is only generated once"""
    with open('key.key','r') as r:
        data = r.read()
        if len(data)<=0:
            key = Fernet.generate_key()
            with open('key.key','wb') as wb:
                wb.write(key)
gen_key()

def load_key():
    """Loading the name key.key"""
    return  open('key.key','rb').read()

key = load_key()
fer = Fernet(key)

def add():
    try:
        user = input('user: ')
        pwd = input('passowrd: ')
        with open('pwd.txt','a') as a:
            a.write(user+"|"+fer.encrypt(pwd.encode()).decode()+"\n")
            print('password saved')
    except:
        print('error while add pwd')

def view():
    try:
        with open('pwd.txt','r') as r:
            for line in r.readlines():
                data = line.rstrip()
                user,pwd = data.split("|")
                print("user: ",user," | pwd: ",fer.decrypt(pwd.encode()).decode())
    except:
        print('error while viewing file')

def main():
    while True:
        user = input('enter add to add pwd and view to view previous pwd and q to quit: ').lower()
        if user == 'q':
            break
        if user=="add":
            add()
        elif user=="view":
            view()
        else:
            print('invalid input')

if __name__=="__main__":
    main()