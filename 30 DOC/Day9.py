def factorial(n):
    fact = 1
    for i in range(n, 0, -1):
        fact = fact * i
    print(fact)
n = int(input())
factorial(n)

# Challenge : Write the following code in 2 lines