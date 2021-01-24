n = int(input())

for i in range(n):
    positions = list(map(int, input().split()))
    if abs(positions[0]-positions[2])<abs(positions[1]-positions[2]):
        print('Cat A')
    elif abs(positions[0]-positions[2])>abs(positions[1]-positions[2]):
        print('Cat B')
    else:
        print('Mouse C')
