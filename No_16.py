def vsota(n):
    stevilo = 2 ** 1000
    c = str(stevilo)
    vsota = 0
    for i in range(len(c)):
        vsota += stevilo % 10
        stevilo //= 10
    return vsota
