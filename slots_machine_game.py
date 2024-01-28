import random

symbols = ['🍒', '🍎', '💵']

while True:
    coins_available = 100
    print('Welcome to the slots game!!!')
    while coins_available > 0:
        print(f'You have {coins_available} coins available.')
        bet = int(input('Bet amount: '))
        if bet > coins_available:
            print('Not enoug coins.')
        else:
            coins_available -= bet
            slot_box_one = random.choice(symbols)
            slot_box_two = random.choice(symbols)
            slot_box_three = random.choice(symbols)

            print()
            print('|', random.choice(symbols), '|', random.choice(symbols), '|', random.choice(symbols), '|')
            print('------------')
            print('|', slot_box_one, '|', slot_box_two, '|', slot_box_three, '|')
            print('------------')
            print('|', random.choice(symbols), '|', random.choice(symbols), '|', random.choice(symbols), '|')
            print()

            if slot_box_one == slot_box_two and slot_box_two == slot_box_three:
                current_win = bet * 5
                print(f'You won {current_win} coins.')
                coins_available += current_win
            else:
                print('You lost this time :-(')
    print('You do not have any coins any more.')
    print('Thanks for playing.')
    print()
