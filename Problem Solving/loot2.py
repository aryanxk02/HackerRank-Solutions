shops = int(input())
coins = list(map(int, input().split()))
M = int(input())
panas = []
sum = 0
min_values = []
for i in range(len(M)):
    P = int(input())
    for j in range(len(shops)):
        for k in range(len(P)):
            sum = min(coins) + max(coins) + sum
            coins.remove(max(coins))
            panas.append(min(coins))
            coins.remove(min(coins))