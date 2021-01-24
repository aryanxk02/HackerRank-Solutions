n = int(input())
s = set(map(int, input().split()))
no_of_commands = int(input())
for i in range(no_of_commands):
    command = input().split(' ')
    if command[0] != 'pop':
        elements = list(map(int, command[-1]))
    if command[0]=='pop':
        s.pop()
    elif command[0]=='remove':
        s.remove(elements[0])
    elif command[0]=='discard':
        s.discard(elements[0])
    else:
        pass
print(sum(s))

