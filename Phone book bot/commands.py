phone_book = {}

def hello():
    print('How can I help you?')


def add(name: str, phone: str):
    phone_book[phone] = name
    


def change(old_phone: str, new_phone: str):
    phone_book[new_phone] = phone_book[old_phone]
    del phone_book[old_phone]
    
    
def phone(name):
    return [k for k, v in phone_book.items() if v == name]


def show_all():
    print(f'Here is your phone book:')
    for k, v in phone_book.items():
        print(f'{k:<15}|{v:<10}')


def main():
    add('Victor', '+308')
    add('Victor', '+30899990454')
    add('Bohdan', '+3809995648')
    # print(phone_book)
    change('+308', '+38099-299-87-89')
    # print(phone_book)
    print(phone('Victor'))
    # show_all()
    
if __name__ == '__main__':
    main()
