shops = int(input())
coins = list(map(int, input().split()))
M = int(input())
panas = []
sum = 0
max_values = []
for i in range(M):
    shops=5
    P = int(input())
    if P==0:
        print('yo')
    else:
        while shops<=5:
            for k in range(P):
                sum = min(coins) + max(coins) + sum
                max_values.append(max(coins))
                coins.remove(max(coins))
                panas.append(min(coins))
                coins.remove(min(coins))
                shops = shops-(len(max_values)+len(panas))
    print('done')
