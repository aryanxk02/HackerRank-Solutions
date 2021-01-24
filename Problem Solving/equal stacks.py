x = list(map(int, input().split()))
a = list(map(int, input().split()))
b = list(map(int, input().split()))
c = list(map(int, input().split()))

a.reverse()
b.reverse()
c.reverse()
a1 = []
b1 = []
c1 = []
# print(a)
for i in range(len(a)):
    a1.append(a[i] + sum(a[:i]))
    # a1.append(a1[i])
for i in range(len(b)):
    b1.append(b[i] + sum(b[:i]))
for i in range(len(c)):
    c1.append(c[i] + sum(c[:i]))
a1.reverse()
b1.reverse()
c1.reverse()
count = [a1, b1, c1]
# small = min(count)
# print(a1)
# print(b1)
# print(c1)
minimum = len(a1)
# if len(a1) == minimum:
#     final = a1
#     ind = count.index(len(a1))
# elif len(b1)==small:
#     final = b1
#     ind = count.index(len(b1))
# else:
#     final = c1
#     ind = count.index(len(c1))`
if len(b1)<minimum:
    small = b1
elif len(c1)<minimum:
    small = c1
else:
    small = a1
count.remove(small)
final = []

# print('count', count)
for i in small:
    if i in count[0] and count[1]:
        print(i)
        break