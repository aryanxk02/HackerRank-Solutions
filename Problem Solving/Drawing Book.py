n = int(input())
p = int(input())

if n-p<=p-1:
    print(int(n-p))
elif n-p == 1:
    print(0)
else:
    print(((p-1)))

# x = []
# x.append(abs(n-p)/2)
# x.append((p-1)/2)
# print(min(x))