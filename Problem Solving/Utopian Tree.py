n = int(input())

height = 0
initial_height = 1

# 1 Spring = 2 * currentheight 1 summer = currentheight + 1

l = []

for i in range(n):
    period = int(input())

    for j in range(period):
        if j == 0:
            print(1)
        elif j%2==0:
            print(j*2 + 1)
        else:
            print()