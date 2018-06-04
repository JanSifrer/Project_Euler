def najvecja_vsota(niz):
    vsota = 0
    i = 0
    while i < len(niz):
        #print(i)
        kandidat = int(niz[i - 3]) * int(niz[i - 2]) * int(niz[i - 1]) * int(niz [i])
        if kandidat > vsota:
            vsota = kandidat
        i += 1
    return vsota
        
def najvecja_vsota_trinajst(niz):
    vsota = 0
    i = 0
    while i < len(niz):
        #print(i)
        kandidat = int(niz[i - 12]) * int(niz[i - 11]) * int(niz[i - 10]) * int(niz [i - 9]) * int(niz[i - 8]) * int(niz[i - 7]) * int(niz[i - 6]) * int(niz [i - 5])* int(niz[i - 4]) * int(niz[i - 3]) * int(niz [i - 2]) * int(niz[i - 1]) * int(niz[i])
        if kandidat > vsota:
            vsota = kandidat
        i += 1
    return vsota        
