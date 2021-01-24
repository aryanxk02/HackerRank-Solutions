n = int(input())
x = 0
count = 0
dummy = True
while dummy:
    n = int(n/2)
    # print('n ;', n)
    # print(type(n))
    count += 1
    if (n)%2 == 1:
        count += 1
        dummy = False
        break
print(count)
# print(int(3/2))