n_d = int(input())

count = 0
d = []
q = []
l = []

for i in range(n_d):
    dictionary = input()
    d.append(dictionary)
# print('d', d)
n_q = int(input())

for j in range(n_q):
    query = input()
    q.append(query)
# print('q', q)
for word in q:
    count=0
    word = list(word)
    # print('word in q', word)
    for word2 in d:
        word2 = list(word2)
        # print('word in d', word2)
        word.sort()
        word2.sort()
        if word==word2:
            # print('word', word)
            # print('word2', word2)
            count += 1

    l.append(count)

            # print(newl)

for m in l:
    print(m)