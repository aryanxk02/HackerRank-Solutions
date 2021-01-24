from collections import deque

n = int(input())
d = deque()
for _ in range(n):
    command = list(map(str, input().split()))
    if command[0] == 'append':
        d.append(int(command[1]))
    elif command[0] == 'appendleft':
        d.appendleft(int(command[1]))
    elif command[0] == 'pop':
        d.pop()
    else:
        d.popleft()
print(*d)