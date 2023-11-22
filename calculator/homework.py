from PY94_GITHOMEWORK.calculator.calculation import summ, multiply, subtraction, divide, exponentiation
from PY94_GITHOMEWORK.calculator.custom_exceptions import WrongNumber, WrongOperation


def user_input():
    while True:
        try:
            first_value = input('Enter first number: ')
            if not first_value.isdigit():
                raise WrongNumber
            second_value = input('Enter second number: ')
            if not second_value.isdigit():
                raise WrongNumber
        except WrongNumber:
            print('Error! Please, enter only numbers:')
        else:
            print(f'Your numbers: {first_value}, {second_value}')
            return int(first_value), int(second_value)


def user_operations():
    affordable_operations = ['+', '-', '*', '/', '**']
    while True:
        try:
            operation = input('What operation do you want to perform with these numbers?: ')
            if operation not in affordable_operations:
                raise WrongOperation
        except WrongOperation:
            print('This operation cannot be used, use another one...')
        else:
            return operation


def calculator(user_values, user_operation):
    try:
        if user_operation == '+':
            print(f'Result - {summ(*user_values)}')
        elif user_operation == '-':
            print(f'Result - {subtraction(*user_values)}')
        elif user_operation == '*':
            print(f'Result - {multiply(*user_values)}')
        elif user_operation == '/':
            print(f'Result - {divide(*user_values)}')
        elif user_operation == '**':
            print(f'Result - {exponentiation(*user_values)}')
    except ZeroDivisionError:
        print('Cant divide by 0')


calculator(user_input(), user_operations())
