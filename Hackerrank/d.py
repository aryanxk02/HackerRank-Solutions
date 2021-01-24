from itertools import combinations
word, numb = input().split(' ')
combo = list(combinations(word, int(numb)))
combo.sort()
[print("".join(i)) for i in combo]