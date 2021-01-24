def makingAnagrams(s1, s2):
    k = [c for c in s1]
    l = list()
    for m in s2:
        if m in k:
            k.remove(m)
        else:
            l.append(m)
    print(len(k)+len(l))
s1 = input()
s2 = input()
makingAnagrams(s1, s2)