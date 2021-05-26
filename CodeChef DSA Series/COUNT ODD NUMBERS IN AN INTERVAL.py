low = int(input())
high = int(input())
count = 0
for i in range(low, high+1):
    print(i)
    if i/2 == 1:
        count += 1
print(count)