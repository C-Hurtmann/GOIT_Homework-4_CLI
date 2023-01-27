import re

import commands as cmd
main_commands = {'add': cmd.add,
                 'change': cmd.change,
                 'phone': cmd.phone,
                 'show all':cmd.show_all
                 }

def find_command_output(func):
    def inner(x):
        if isinstance(func(x), str):
            pass
        elif func(x):
            print("I think, I didn't understand you clearly.\nDid you mean", end=' ') 
            print(*func(x), sep=' or ', end='?\n')
        else:
            print("Sorry, I didn't understand you at all") 
            print('Here in a list of commands i know:', *list(sorted(main_commands.keys())), sep='\n')
    return inner


@find_command_output
def find_command(user_input: str):
    user_input = user_input.lower()
    if user_input in main_commands: 
        return user_input.lower() #for complete match
    result = []
    for req in main_commands.keys(): 
        searching = re.search(r'{}'.format(req), user_input)
        if searching:
            result.append(searching.group())
    return result #for particylar match

        

def testing():
    find_command('add')
    # find_command('Add someone to mine phone book')
    # find_command('Could YOU ADD this number to my phone book')
    # find_command('Could you show me phone number without adding to my phone book?')
    # find_command('123')
    
if __name__ == '__main__':
    testing()