n = int(input())
l = list(map(int, input().split()))

# final = [True if all([l[i]>0]) and any(list(l[i]).reverse()==l[i]) else False for i in range(len(l))]
print(all(l[i]>0 for i in range(len(l))))
# print(all(l[i]>0 for i in range((l))) and any([l[j] == l[j[::-1]] for j in (l)]))
# for j in range(len(l)):
#     if any(str(l[j])==str(l[j[::-1]])):
#         print(True)
#     else:
#         print(False)

# print(all([int(i)>0 for i in l]) and any([j==j[::-1] for j in l]))

