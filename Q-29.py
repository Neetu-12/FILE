# n=int(input("enter the no."))
# i=1
# s1=0
# while i<=n:
#     j=0
#     s2=0
#     while j<=10:
#         a=j*5
#         s2=s2+a
#         j=j+1
#     b=i*5
#     s1=s1+b
#     i=i+1
#     print(s2,s1)


def add(m):
    i=1
    r=[]
    while i<=n:
        a=i**2
        r.append(a)
        i=i+1
    return r
n=int(input("enter the no."))
print(add(n))