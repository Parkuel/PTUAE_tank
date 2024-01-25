
def print_menu():
    menu = ['1. Start Game', '2. Display Info', '3. Exit']
    for item in menu:
        print(item)


def take_input():
    while True:
        try:
            prompt = int(input('Enter a command (1-3): '))
            if prompt not in range(1, 4):
                print('Invalid Command. Enter numbers between 1 - 3')
            else:
                break
                
        except ValueError:
            print('Invalid Command. Enter a number')
    return prompt

# print(take_input())
