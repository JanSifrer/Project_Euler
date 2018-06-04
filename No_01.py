def vsota_veckratnikov(n):
    vsota = 0
    for i in range(1, n):
        if i % 3 == 0:
            vsota += i
        elif i % 5 == 0:
            vsota += i
    return vsota
