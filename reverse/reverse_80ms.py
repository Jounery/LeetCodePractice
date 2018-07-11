def reverse(x):
        L = []
        if abs(x) > 2147483647:
            flag = 0
        elif x < 0:
            flag = -1
        else:
            flag = 1
        x = abs(x)
        while x >= 1:
            a = x %10
            x = int(x / 10)
            L.append(a)
        num = 0
        for i in L:
            num = num*10 + i
        if num > 2147483647:
            num = 0
        return num*flag
