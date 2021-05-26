A = [1, 1, 2]
x = []
count = 0
for i in A:
    if i not in x:
        x.append(i)

# print(len(A) - (len(A) - len(x)))
# print(len(x))
print(x)