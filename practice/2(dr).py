import random
def bd_par(p,n=23):
    c = 0
    for l in range (p):
        bd = []
        for r in range (n):
            d=random.randrange(0,365)
            bd.append(d)
        sbd=set(bd)
        if len(sbd)<len(bd):
            c+=1
    proc=(c*100)/p
    return proc


if __name__ == '__main__':

    print(bd_par(1000,23))
