english = int(input())
s1 = set(map(int, input().split()))
french = int(input())
s2 = set(map(int, input().split()))
print(len(s1.symmetric_difference(s2)))

#set a + set b - set a intersection set b

