def vsota(n):
    resitev = 0
    for i in range(1, n + 1):
        resitev += i ** i
    return resitev % 10000000000
