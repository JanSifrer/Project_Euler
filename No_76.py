def na_koliko_nacinov(n):
    nacin = 0
    if n == 1:
        nacin += 1
    if n > 1:
        nacin += 1 + na_koliko_nacinov(n - 1)
    return nacin
        
