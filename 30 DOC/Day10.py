def DecimalToBinary(num):

        count = 0

        if num > 1:
            DecimalToBinary(num // 2)
            a = num % 2

            for i in str(a):

                if  str(a[i]) == str(a[i + 1]):
                    count += 1
                else:
                    break

num = int(input())
DecimalToBinary(num)