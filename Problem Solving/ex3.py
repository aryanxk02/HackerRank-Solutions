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
for i in n:
    a = []
    for j in range(3):
        a.append(i[j])
# ignore file