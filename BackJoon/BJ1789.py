n = int(input());

a = 1
while 1:
    temp = a * (a+1) / 2
    if temp > n:
        a = a - 1;
        break
    else:
        a = a + 1

print(a)