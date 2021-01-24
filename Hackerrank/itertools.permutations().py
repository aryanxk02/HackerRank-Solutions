# n = input().split()
# l = []
# for char in n[0]:
#     l.append(char)
# print(l)
# for k in range(len(l)):
#     for i in range(0, int(n[1])):
#         for j in range(i, int(n[1])):
#             print(str(l[i])+str(l[j]))

from itertools import permutations

word, num = input().split(" ")
pmt = list(permutations(word, int(num)))
# print(pmt)
a=pmt.sort()
# print(a)
[print("".join(i)) for i in pmt]