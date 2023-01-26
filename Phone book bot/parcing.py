import re

import commands

main_commands = {'add': commands.add,
                 'change': commands.change,
                 'phone': None,
                 'show all':None
                 }



def find_command(user_input: str):
    user_input = user_input.lower()
    if user_input in main_commands: 
        return user_input.lower() #for complete match
    result = []
    for req in main_commands.keys(): 
        searching = re.search(r'{}'.format(req), user_input)
        if searching:
            result.append(searching.group())
    print("I think, I didn't understand you clearly.\nDid you mean", end=' ') #for particylar match
    print(*result, sep=' or ', end='?\n')  
        
    #print("Sorry, I didn't understand you at all") 
    #print('Here in a list of commands i know:', *list(sorted(requests.keys())), sep='\n')
        

def testing():
    # print(find_command('Add someone to mine phone book'))
    print(find_command('Could YOU ADD this number to my phone book'))
    # print(find_command('Could you show me phone number without adding to my phone book?'))
    
    
if __name__ == '__main__':
    testing()