n=int(input("enter the no"))
i=1
r=[]
s=[]
n1=[]
while i==1:
    if n==1:
        c="A1,B1"
        n1.append(c)
        print(n1)
    elif n==2:
        a="A1,B1,A2,B2"
        s.append(a)
        print(s)
    elif n==3:
        b="A1,B1,A2,B2,A3,B3"
        r.append(b)
        print(r)
    else:
        print("nothing")
    i=i+1