def je_deljivo_s_katerim_od(n, seznam):
    for i in seznam:
        if n % i == 0:
            return True
    return False

def prastevila_do(n):
    r = 0
    if n < 2:
        return []
    r = 2
    for i in range(3, n):
        if not je_deljivo_s_katerim_od(i, range(2, i)):
            r += i
        print(r)
    return r

def vsota(n):
    a=2
    p=0
    while a<2000000:
        b= int(a**0.5) 
        for x in range(2,b+1):
            if a%x==0:
                break
        else:
            p+=a
            print(p)
        a+=1
    print(p)

142913828922
