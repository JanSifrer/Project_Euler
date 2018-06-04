def fakulteta(n):
    if n == 1:
        return 1
    else:
        return n * fakulteta(n - 1)

def vsota(n):
    stevilo = fakulteta(n)
    dolzina = str(stevilo)
    m = len(dolzina)
    rezultat = 0
    while m > 0:
        if stevilo > 10:
            rezultat += stevilo % 10
            stevilo //= 10
            m -= 1
        else:
            rezultat += stevilo
            m -= 1
    return rezultat
            
    
