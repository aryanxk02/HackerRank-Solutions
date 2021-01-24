grid = int(input())
x, y = input().split()
x=int(x)
y=int(y)
n=int(input())

negatives = []

for i in range(n):
    command = input().split( )
    command[1] = int(command[1])

    if command[0] == 'N':
        y = y - int(command[1])
        if 1 > y or y > 10:
            negatives.append(i)
    if command[0] == 'S':
        y = y + int(command[1])
        if 1 > y or y > 10:
            negatives.append(i)
    if command[0] == 'E':
        x = x + int(command[1])
        if 1 > x or x > 10:
            negatives.append(i)
    if command[0] == 'W':
        x = x - int(command[1])
        if 1 > x or x > 10:
            negatives.append(i)


if len(negatives)==0:
    print(x, y)
else:
    print('FALL')

