"""
Prints prime numbers
A prime number is a natural number greater than 1 that is not a product of two smaller natural numbers.
The first ten primes are 2, 3, 5, 7, 11, 13, 17, 19, 23, 29.
"""


def main():
    print('A prime number is a natural number greater than 1 that is not a product of two smaller natural numbers.')
    print('This program\'s soul purpose is to print prime numbers')
    f, t = choice1()
    c = input('Enter 0 if you don\'t want the steps ')
    if c == '0':
        choice2(f, t)
    else:
        steps(f, t)


def choice2(f, t):
    """
    In this program I use a nested for loop to crate one column being tested 'n' by the column m.
    For everytime n loop starts, m tests if n is a prime number by dividing n by m from 2 too n excluding n,
    and testing for remainders with he remainder operator %
    """
    for n in range(f, t):
        if n > 1:
            for m in range(2, n):
                if n % m == 0:
                    break
            else:
                print(n)


def steps(f, t):
    for n in range(f, t):
        # creates range (column) to look for prime numbers
        # for n in range(2, 100 + 1):
        if n > 1:
            # if statement skips 1 and 0 in for loop
            for m in range(2, n):
                # since 1 divided by any number has a remainder of 0 skip 0
                # divide every number from 2 to the number being tested except the number being tested (5 % 5 = 0)
                # test if remainder % is 0
                # if remainder is 0 break and test new number
                print(n, 'divided by', m, 'has a remainder of', n % m)
                if n % m == 0:
                    print(n, 'is not prime')
                    break
            else:
                # if no break was triggered
                print('~', n, '~', 'is a prime number')
            """
            I learned that putting an else 'clause' outside of a for loop acts as: 'if loop was never broken do this'
            How I understand it is the else statement need to be outside to allow the loop to check for every number
            without triggering the else statement before every number is checked. for example:
            When the else statement is inside the for loop, the loop tries to divide 15 by 2, it finds a remainder of 1,
            and
            prints it as a prime number although 15 is not prime because 3 * 5 = 15. 3 is the next number to be tested 
            to give a result of not prime (composite)
            """


def choice1():
    f = input('Input start range or press enter to default to 2 ')
    t = input('Input stop range or press enter to default to 24 ')
    if f == '':
        f = 2
    if t == '':
        t = 24
    f = int(f)
    t = int(t)
    t += 1
    return f, t


if __name__ == '__main__':
    main()
