from collections import deque
def playingWithNumbers(arr1, arr2):
    for i in arr2:
        # l  =deque()
        l = deque(i + num for num in arr1)
        # l_new = deque(abs(j) for j in l)
        l = deque(map(lambda x: x + i, arr1))
        l_new = list(map(abs, l))
        # print(l_new)
        arr1 = l
        print(sum(l_new))
n = int(input())
arr1 = deque(map(int, input().split()))
m = int(input())
arr2 = deque(map(int, input().split()))
playingWithNumbers(arr1, arr2)