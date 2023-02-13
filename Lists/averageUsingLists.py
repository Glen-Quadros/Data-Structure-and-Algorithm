list = []

while(True):
    inp = input('Enter a number: ')
    if inp == 'done':
        break
    values = int(inp)
    list.append(values)
avg = sum(list)/len(list)

print('Average: ' + str(avg))