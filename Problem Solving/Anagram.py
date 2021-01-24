def anagram(t):
    for _ in range(t):
        s = input()
        count = 0
        if len(s)%2==1:
            print(-1)
        else:
            a = (s[:int(len(s)/2)])
            b = list(s[int(len(s)/2):])
            for letter in a:
                if letter in b:
                    b.remove(letter)
                else:
                    count += 1
            print(count)

t = int(input())
anagram(t)

# asdfjoieufoa
# 3
# fdhlvosfpafhalll
# 4
# mvdalvkiopaufl
# 5
