def razlika_vsot(n):
    vsota = 0
    vsota_2 = 0
    for i in range(1, n + 1):
        vsota += i ** 2
    for j in range(1, n + 1):
        vsota_2 += j
    vsota_2 = vsota_2 ** 2
    return vsota_2 - vsota
