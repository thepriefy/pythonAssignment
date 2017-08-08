def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

while True:
    try:
        print("Enter your INTEGER value of X and press Enter")
        x = int(input('X: '))

        print("Enter your INTEGER value of Y and press Enter")
        y = int(input('Y: '))

        # X+Y
        print('X+Y: ', x + y)

        # X-Y
        print('X-Y: ', x - y)

        # X*Y
        print('X*Y: ', x * y)

        # X^Y
        print('X^Y: ', x ^ y)

        # X!
        print('X!: ', factorial(x))

        # Y!
        print('Y!: ', factorial(y))

        # X/Y
        print('X/Y: ', x / y)

        # X//Y
        print('X//Y: ', int(x / y))

        # X%Y
        print('X%Y: ', x % y)

        print("========== End ==========")

    except ValueError:
        print('Please input an INTEGER...')
