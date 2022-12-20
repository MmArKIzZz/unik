a=int(input())
b=0
c=[]
while 2**b<=a:
    b+=1
print(b-1,2**(b-1))