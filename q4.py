def hcf(a,b):
    first = a
    second = b
    if second > first:
        a = second
        b = first
    else:
        a = first
        b = second
    while True:
        if a%b == 0:
            print('hcf is '+ str(b))
            return(b)
        x = a%b
        a = b
        b = x


s = 0
for i in range(1,1112):
    s+= hcf(i,1111)
    print(s)