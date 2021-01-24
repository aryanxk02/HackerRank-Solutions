n = int(input())
l = []
for i in range(n):
    command = input().split(' ')
    positions = list(map(int, command[1:]))
    if command[0]=='insert':
        l.insert(positions[0], positions[1])
    elif command[0]=='print':
        print(l)
    elif command[0]=='remove':
        l.remove(positions[0])
    elif command[0]=='append':
        l.append(positions[0])
    elif command[0]=='sort':
        l.sort()
    elif command[0]=='pop':
        l.pop
    elif command[0]=='reverse':
        l.reverse()
    else:
        pass
