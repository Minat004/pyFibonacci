def fibo(num):
    if num == 1:
        return 0
    elif num == 2:
        return 1
    else:
        return fibo(num - 1) + fibo(num - 2)


if __name__ == '__main__':
    check = True
    while check:
        try:
            number = int(input('Please write Fibonacci number: '))
            while number <= 0:
                number = int(input('Fibonacci number need to be positive, try again: '))
        except ValueError as error:
            print('Fibonacci number is wrong value, try again: ')
            continue
        else:
            print(f'Fibonacci element is {fibo(number)}')
            check = False