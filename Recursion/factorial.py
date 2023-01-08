# Find the factorial of a number using recursion

def factorial(n):
    assert n >= 0 and int(n) == n, 'Enter a positive integer'
    if n in [0,1]:
        return n
    else:
        return n * factorial(n-1)

number = input('Enter a number: ')
print(factorial(int(number)))