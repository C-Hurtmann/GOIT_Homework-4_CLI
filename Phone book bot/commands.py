phone_book = {}

def hello() -> str:
    return 'How can I help you?'


def add(name: str, phone: str) -> str:
    if not phone_book.get(name):
        phone_book[name] = phone
        return f'{name} has been saved in your phone book with number {phone}'
    return f'{name} has already existed in your phone book. Number is {phone_book.get(name)}'


def change(name: str, new_phone: str) -> str:
    old_phone = phone_book.get(name)
    if old_phone:
        phone_book[name] = new_phone
        return f'For {name} the number has been changed from {old_phone} to {new_phone}'
    return f'No such user in your phone book'
    
    
def phone(name) -> str:
    if phone_book.get(name):
        return f'Phone of {name} is {phone_book.get(name)}'
    return f'{name} has not been recorded in your phone book'


def show_all() -> str:
    result_table = ['Here is your phone book:']
    for k, v in phone_book.items():
        result_table.append(f'{k:<10}|{v:<10}')
    return '\n'.join(result_table)


def tests():
    print(hello())
    print(add('Victor', '+308'))
    print(add('Victor', '+30899990454'))
    print(add('Bohdan', '+3809995648'))
    print(phone_book)
    change('+308', '+38099-299-87-89')
    print(phone('Victor'))
    print(show_all())
    
if __name__ == '__main__':
    tests()
