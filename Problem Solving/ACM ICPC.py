n, m = input().split()
n = int(n)
m = int(m)

topics = []

for i in range(n):
    # inputArrays = ((input()))
    topics.append(input())

l = []
n1 = []
n2 = []
final = []
# print('topics =', topics)
for i in range(0, n - 1):
    for num in str(topics[i]):
        n1.append(int(num))
    # print('n1 =', n1)
    for k in range(i + 1, n):
        # print('k =', k)
        for num2 in (topics[k]):
            # if k==3:
            #     print('Value of num2 =', num2)
            n2.append(int(str(num2)))
        # print('n2 =', n2)
        for j in range(m):
            # print(j)
            # value = n1[j] | n2[j]
            l.append(n1[j] | n2[j])
        final.append(l.count(1))
        # print('l =', l)
        l = []
        n2 = []

# print('l =', l)
# print('final =', final)
print(max(final))
print(final.count(max(final)))