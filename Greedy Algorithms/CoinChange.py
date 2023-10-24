def coinChange(totalNumber, coins):
    N = totalNumber
    coins.sort()
    lastIndex = len(coins) - 1

    while True:
        coinValue = coins[lastIndex]
        if N >= coinValue:
            print(coinValue)
            N -= coinValue
        if N < coinValue:
            lastIndex -= 1
        if N == 0:
            break

coins = [1,2,5,20,50,100]
coinChange(201, coins)