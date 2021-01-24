# t = int(input())
# for _ in range(t):
#     l = list(map(int, input().split()))
#     R = l[0]
#     C = l[1]
#     mat = []
#     for i in range(R):
#         inpstr = input()
#         mat.append(inpstr)
#     # print('mat:', mat)
#     x = list(map(int, input().split()))
#     r = x[0]
#     c = x[1]
#     mat2 = []
#     for i in range(r):
#         inpstr2 = input()
#         mat2.append(inpstr2)
#     # print('mat2', mat2)
#     count = 0
#     for i in mat2:
#         for j in mat:
#             if i in j:
#                 count = 1
#     if count == 1:
#         print('YES')
#     elif count == 0:
#         print('NO')
t = int(input())
for _ in range(t):
    l = list(map(int, input().split()))
    R = l[0]
    C = l[1]
    mat = []
    for i in range(R):
        inpstr = input()
        mat.append(inpstr)
    # print('mat:', mat)
    x = list(map(int, input().split()))
    r = x[0]
    c = x[1]
    mat2 = []
    for i in range(r):
        inpstr2 = input()
        mat2.append(inpstr2)
    def grid(mat, mat2):

        def check(x, y):
            for i in range(r):
                if mat2[i] != mat[x+i][y:y+c]:
                    return False
            return True
    for i in range(R):
        for j in range(C):
            if mat[i][j] == mat2[0][0]:
                if check(i,j):
                    return 'YES'
        return 'NO'
    check(x, y)