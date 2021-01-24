n = int(input())
array = list(map(int, input().split()))

a = array.count(1)
b = array.count(2)
c = array.count(3)
d = array.count(4)
e = array.count(5)

l = [a, b, c, d, e]

print(1+l.index(max(l)))


