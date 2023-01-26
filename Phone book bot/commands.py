phone_book = {}


def add(name: str, phone: str):
    phone_book[phone] = name
    


def change(old_phone: str, new_phone: str):
    phone_book[new_phone] = phone_book[old_phone]
    del phone_book[old_phone]


def main():
    add('Victor', '+308')
    add('Bohdan', '+3809995648')
    print(phone_book)
    change('+308', '+38099-299-87-89')
    print(phone_book)
    
    
if __name__ == '__main__':
    main()
