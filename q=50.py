a=['I am Neetu Sah']
i=0
while i<len(a):
    j=0
    while j<len(a[i]):
        c=a[i].split(" ")
        j=j+1
    i=i+1
    print(c)

b=['a',1, '2' ,5, 'b','q']
i=-1
while i>=-1:
    n=int(input("enter the no."))
    if n==1:
        print("q")
    elif n==2:
        print("b q")
    elif n==3:
        print("5 b q")
    elif n==4:
        print("2 5 b q")
    elif n==5:
        print("1 2 5 b q")
    elif n==6:
        print("a 1 2 5 b q")
    else:
        print("nothing")
    i=i-1