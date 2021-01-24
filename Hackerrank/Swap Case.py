# a = input()
# l = a.split(' ')
# j = ''.join(l)
# for i in range(0, len(a)):
#     if i == i.lower() :

# print(''.join([i.upper(i)]))

def swap_case(s):
    x = (s.swapcase())
    return x
if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)

# a = input()
# print(a.swapcase())