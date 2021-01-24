def viralAdvertising(n):
    shared = 5
    liked = 0
    cumulative = 0

    for day in range(n):
        liked = int(shared / 2)
        cumulative += liked
        shared = 3 * liked

    print(cumulative)
n = int(input())
viralAdvertising(n)