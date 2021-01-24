def hurdleRace(max_height, heights):
    if max_height >= max(heights):
        print(0)
    else:
        print(max(heights) - max_height)


n_hurdles, max_height = input().split()

n_hurdles = int(n_hurdles)
max_height = int(max_height)

heights = list(map(int, input().split()))

hurdleRace(max_height, heights)