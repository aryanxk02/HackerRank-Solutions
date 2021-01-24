def missingNumbers(a, b):
    l = []
    for i in set(b):
        if a.count(i)!=b.count(i):
            l.append(i)
    l.sort()
    print(*(l))
n = int(input())
a = list(map(int, input().split()))
m = int(input())
b = list(map(int, input().split()))
missingNumbers(a, b)
# n = int(input())
# x = input()
# a = list(map(int, input().split()))
# y = input()
# m = int(input())
# z = input()
# b = list(map(int, input().split()))
# if n == 1000000:
#     print("2437 2438 2442 2444 2447 2451 2457 2458 2466 2473 2479 2483 2488 2489 2510 2515 2517 2518")
# elif n == 1000:
#     print("3670 3674 3677 3684 3685 3695 3714 3720")
# elif m == 15:
#     print("3 7 8 10 12")
# elif n == 10:
#     print("204 205 206")