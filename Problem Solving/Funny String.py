n = int(input())

# l = [] # ascii for a
# l2 = l[::-1] # ascii for rev_a
# l3 = [] # ascii for b
# l4 = l3[::-1] # ascii for rev_b

for _ in range(n):
    a = input()
    rev_a = a[::-1]

    l = []  # ascii for a
    common = []
    for i in a:
        common.append(i)

    for i in common:
        l.append(ord(i))

    l2 = l[::-1]  # ascii for rev

    for i in range(len(l)-1):
        if abs(l[i]-l[i+1]) == abs(l2[i]-l2[i+1]):
            pass
        else:
            print('Not Funny')
