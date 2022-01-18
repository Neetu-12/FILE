
# a= [10, 14, 2, 23, 19] #-->  42 (= 23 + 19)
# max=0
# smax=0
# i=0
# while i<len(a):
#     if a[i]>max:
#         smax=max
#         max=a[i]
#     if a[i]>smax and a[i]<max:
#         smax=a[i]
#     i=i+1
# p=(smax+max)
# print(max,"+",smax,"=",p)



def add(m):
    max=0
    smax=0
    i=0
    while i<len(m):
        if m[i]>max:
            smax=max
            max=m[i]
        if m[i]>smax and m[i]<max:
            smax=m[i]
        i=i+1
    p=(smax+max)
    return max, "+" ,smax, "=", p
n= [10, 14, 2, 23, 19]
print(add(n))


def sub(n):
    max=0
    smax=0
    i=0
    while i<len(n):
        if n[i]>max:
            smax=max
            max=n[i]
        if n[i]>smax and n[i]<max:
            smax=n[i]
        i=i+1
    p=(smax+max)
    return max,"+",smax,"=",p
b=[99, 2, 2, 23, 19]
print(sub(b))