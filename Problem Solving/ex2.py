arr = input()
tn = int(arr[0])
tq = int(arr[2])
n = []
q = []
for i in range(tn):
    we_have = list(map(int, input().split()))
    n.append(we_have)
for i in range(tq):
    we_req = list(map(int, input().split()))
    q.append(we_req)
x = []
for i in range(3):
    a = []
    for j in n:
        a.append(j[i])
    x.append(a)
R = x[0]
G = x[1]
B = x[2]
j = 0
# for i in q:
#     if i[j] in R and i[j+1] in G and i[j+2] in B:
#         print('YES')
#     else:
#         print('NO')
c = [print('YES') for i in q if i[j] in R and i[j+1] in G and i[j+2] in B]
if c == 'YES':
    pass
else:
    print('NO')