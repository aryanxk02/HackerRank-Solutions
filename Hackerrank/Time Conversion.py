h, m, s = str(input()).split(':')
H = int(h)

if 'AM' in s:
    if H>=1 and H<12:
        print(h,':',m,':',s[0:2])
    elif H==12:
        H=str(00)
        print(H,':',m,':',s[0:2])
    else:
        pass

if 'PM' in s:
    if H>=1 and H<12:
        H=H+12
        print(H,':',m,':',s[0:2])
    if h==12:
        h[0:2]==0
        print(h,':',m,':',s[0:2])


