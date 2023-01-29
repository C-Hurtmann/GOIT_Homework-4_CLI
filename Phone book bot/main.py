from parcing import command_launch

if __name__ == '__main__':
    print('Bot awakened.')
    while True:
        user_input = input('Enter your request:')
        print(command_launch(user_input))
        print('-' * 50)