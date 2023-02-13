noOfDays = int(input('Enter the number of days: '))
totalTemp = []

for i in range(noOfDays):
    temp = int(input('Day ' + str(i + 1) + ' highest temperature: '))
    totalTemp.append(temp)
    total = sum(totalTemp)

avg = total / noOfDays

print('Average: ' + str(avg))

count = 0
for i in totalTemp:
    if i > avg:
        count = count + 1

print('No. of day(s) the temperature is above average is ' + str(count))