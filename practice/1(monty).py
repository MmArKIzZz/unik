import random
def monty(t):
    w=0
    a=[0,1,0]
    v=0
    for i in range(t):
        i=+1
        a=[0,1,0]
        n=random.choice(a)
        a.remove(n)
        if n==1:
            w+=1
            v+=1
        a.remove(0)
        if a[0]!=1:
            w+=1
    return round((w/t*100),3),round((v/t*100),3)
if __name__=='__main__':
    print(monty(100))
