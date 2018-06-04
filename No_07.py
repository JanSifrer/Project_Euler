def je_prastevilo(n):
    if n < 2:
        return False
    else:
        for i in range(2, n):
            if n % i == 0:
                return False
        return True

def n_to_prastevilo(x):
    resitev = []
    n = 2
    k = 0
    while len(resitev) < x:
        #print('ali je', n)
        if je_prastevilo(n):
            resitev += [n]
            print(n,'je', k, 'praštevilo',)
            k += 1
        n += 1
    return resitev[-1]
