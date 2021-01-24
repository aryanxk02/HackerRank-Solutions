# string = input()
# s, c = input().split()
# l = list(string)
# l[int(s)] = c
# newl = ''.join(l)
# print(newl)


# approach 2
# string = input()
# s, c = input().split()
# l1 = list(string[:int(int(s)-1)])
# print(l1)
# l2 = list(string[int(s):])
# print(l2)
# l3 = list(c)
# print(l3)
# lsum = l1+l3+l2
# newnew = ''.join(lsum)
# print(newnew)

# string = input()
# i, c = input().split()
# string = string[:int(i)] + str(c) + string[int(int(i) + 1):]
# print(string)

def mutate_string(s, i, c):
    return s[:int(i)] + str(c) + s[int(int(i)+1):]


if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)