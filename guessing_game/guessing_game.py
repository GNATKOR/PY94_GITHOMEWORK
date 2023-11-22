from random import randint


def game():
    def get_range():
        while True:
            u_from = int(
                input('Warning!!! The range must contain at least 5 digits and no more than 30\nEnter range from: '))
            u_to = int(input('to..: '))
            if 5 <= ((u_to + 1) - u_from) <= 30:
                break
            else:
                print('Incorrect range. Try again.')
        return u_from, u_to

    def random():
        a, b = get_range()
        random_set = set()
        while len(random_set) < 3:
            random_set.add(randint(a, b))
        print(f'Interpreter made this numbers: {list(random_set)}')  # this stroke added only for debug
        return random_set

    def user_list():
        empty_list = []
        for i in 1, 2, 3:
            a = input('Enter number: ')
            if a == 'exit':
                quit()
            else:
                empty_list.append(a)
        user_list = [int(x) for x in empty_list]
        return user_list

    def game_check():
        comp_list = random()
        while True:
            guessed_num = set()
            for i in user_list():
                if i in comp_list:
                    guessed_num.add(i)
            if len(guessed_num) == 3:
                print('You win!')
                break
            else:
                print(f'Try again, you guessed {len(guessed_num)} of numbers')

    game_check()


game()
