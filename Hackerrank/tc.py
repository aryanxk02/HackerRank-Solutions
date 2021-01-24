h = input()
time=h.split(':')

if time[0]==str(12) and "AM" in time[2]:
    time[0]=str(0)+str(0)
    newtime = ':'.join(time)
    print(newtime[:-2])
elif int(time[0])>=(1) and int(time[0])<(12) and 'AM' in time[2]:
    print(h[:-2])
else:
    pass

if int(time[0])>=(1) and int(time[0])<(12) and 'PM' in time[2]:
    time[0] = str(int(time[0]) + 12)
    newtime = ':'.join(time)
    print(newtime[:-2])
elif int(time[0])==12 and 'PM' in time[2]:
    newtime = ':'.join(time)
    print(newtime[:-2])
else:
    pass

