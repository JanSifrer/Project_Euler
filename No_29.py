def stevilo_elementov(n):
    stevilo = []
    for a in range(2, 101):
        for b in range(2, 101):
            c = a ** b
            if not c in stevilo:
                stevilo += [c]
    return len(stevilo)
