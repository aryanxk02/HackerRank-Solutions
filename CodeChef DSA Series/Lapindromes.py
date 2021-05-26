t = int(input())
for _ in range(t):
    s = input()
    if len(s) % 2 != 0:
        s1 = s[:len(s)//2]
        s2 = s[(len(s)//2)+1:]
    else:
        s1 = s[:len(s)//2]
        s2 = s[len(s)//2:]
    if sorted(s1) == sorted(s2):
        print("YES")
    else:
        print("NO")