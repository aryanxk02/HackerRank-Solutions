def year(a):
    if a%4 == 0:
        if a%100 == 0:
             if a%400 == 0:
                it_is = True
                print(it_is)
    else :
        if (a%4 != 0):
            it_is = False
        elif (a%100 != 0):
            it_is = False
        else :
            (a % 400 != 0)
            it_is = False
        return it_is

enter_year = int(input())
year(enter_year)

