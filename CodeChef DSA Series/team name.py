t = int(input())
for x in range(t):
    n = int(input())
    words = input().split()
    d = {}
    count = 0
    for i in words:
        d[words[1:]] = words[i][0]

    letters = []
    for i in d.keys():
        letters.append(i)
    letters = set(letters)

    for i in letters:
        for j in d:
            if i in j.keys():
                count += 1
    print(count*2)
# d = {"ell":['h','b'], "est":['b','t']}
# for i in d:
#     print(i)