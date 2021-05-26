pos = int(input())
n = 0
i = 0
count = -1
if pos == 0:
    print(0)
for i in range(pos):
    n = n + i
    count += 1
    # print("n : ", n)
    if pos == n :
        break
    elif pos < n:
        # count += 1
        for j in range(pos):
            n = n - j
            count += 1
            # print("j : ", j, ",n : ", n)
            if pos == n:
                break
            break
        break

print(count)
