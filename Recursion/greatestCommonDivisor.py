# Find the greatest common divisor of two numbers

def gcd(a, b):
    assert int(a) == a and int(b) == b, 'Numbers must be intergers'
    if a < 0:
        a = a * -1
    if b < 0:
        b = b * -1
    if b == 0:
        return a
    return gcd(b, a%b)

print(gcd(48, 18))