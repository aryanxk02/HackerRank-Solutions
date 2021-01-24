n = int(input())
a = list(map(int, input().split()))
max_in_a = max(a)
a.remove(max(a))
b = a
while max(b) == max_in_a:
    b.remove((max(b)))
print(max(a))