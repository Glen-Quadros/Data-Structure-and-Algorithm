def fibNumbersMemo(n, memo):
    if n == 1:
        return 0
    if n == 2:
        return 1
    if n not in memo:
        memo[n] = fibNumbersMemo(n-1, memo) + fibNumbersMemo(n-2, memo)
    return memo[n]

myDict = {}
print(fibNumbersMemo(6, myDict))    