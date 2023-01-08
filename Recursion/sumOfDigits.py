# Find the sum of digits of a positive number using recursion

def sumOfDigits(n):
    assert n >= 0 and int(n) == n, 'Enter a positive integer'
    if n == 0:
        return 0
    else:
        return int(n%10) + sumOfDigits(int(n/10))

num = input('Enter a number: ')
print(sumOfDigits(int(num)))