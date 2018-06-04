def najvecje_stevilo(x):
    #namesto x-a ustavi katero koli število :)
    kandidat = []
    for i in range(10000, 1000000):
        i = str(i)
        ali_je = True
        j = 0
        while j <= (len(i) / 2):
            if i[j] == i[- 1 - j]:
                #print(j)
                j += 1
            else:
                ali_je = False
                j += 1
        if ali_je == True:
            kandidat += [i]
            #print(kandidat)
    #print(kandidat)
        
    najvecje_stevilo = 0
    for i in range(len(kandidat)):
        for j in range(100, 1000):
            if int(kandidat[i]) % j == 0:
                #print(int(kandidat[i]),j)
                if 100 < int(kandidat[i]) /  j  < 1000:
                    #print(int(kandidat[i]),j)
                    najvecje_stevilo = int(kandidat[i])
    return najvecje_stevilo
            
    
