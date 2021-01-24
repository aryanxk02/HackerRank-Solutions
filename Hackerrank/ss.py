def reverse_words_order_and_swap_cases(n):
    l = []

    for word in n:
        l.append(word.swapcase())

    l.reverse()

    print(*l)

n = input().split(' ')
reverse_words_order_and_swap_cases(n)

