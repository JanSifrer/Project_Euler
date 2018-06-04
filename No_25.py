def fibonacci(n):
    a, b = 0, 1
    while n > 0:
        c = a + b
        a = b
        b = c
        n -= 1
    return a
#fibonacci je definiran z zanko
i = 1
while fibonacci(i) < 10 ** 999:
    i += 1
print(i)

#Na 999 je zato, ker me zanima prva številka ki je od tega večja.. npr. od 99 je
#naslednja večja številka 100, če pa bi napisu <100, bi pa dobu št. ki je čist
#mau večja od 100. ker me pa zanimajo številke manše od 100, moram uporabiti
#prvi način.
