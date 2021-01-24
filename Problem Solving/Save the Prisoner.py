test_cases = int(input())

for i in range(test_cases):
    prisoners, candies, starting_point = input().split()
    prisoners = int(prisoners)
    candies = int(candies)
    starting_point = int(starting_point)
    a = (starting_point + candies - 1)  % prisoners
    if a == 0:
        print(int((starting_point + candies - 1) / prisoners))
    else:
        print(a)