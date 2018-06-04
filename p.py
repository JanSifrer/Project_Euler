def vsota(n):
    s = list(range(0, n+1))
    s[1] = 0
    i = 2
    while i*i <= n:
        for j in range(2*i,n + 1, i):
            s[j] = 0
        i += 1
    return sum(s)
