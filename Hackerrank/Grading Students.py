# print(74%5) #1
# print(73%5) #2
# print(72%5) #3

def grade(n):
    l = []
    for a in range(0, n):
        a = int(input())

    if a >= 38:
        if a % 5 >= 3:
                final_marks = a + 5 - a % 5
                l.append(final_marks)

        # elif a % 5 < 3:
        #         l.append(a)
        #
        #
        # else:
        #         pass
        else:
            l.append(a)

        if a <= 37:
            l.append(a)

    return l

n = int(input())
l=[]
print(grade(n))


# def add(x, y):
#     z = x+y
#     print(z)
# x = input()
# y = input()
# add(x,y)


