# def add():
#     n=int(input("enter the no."))
#     i=2
#     while i<=n:
#         j=1
#         c=0
#         while j<=i:
#             if i%j==0:
#                 c=c+1
#             j=j+1
#         i=i+1
#     if c==2:
#         print("prime no.")
#     else:
#         print("not prime")
# add()

# def add(a):
#     i=2
#     while i<=n:
#         j=1
#         c=0
#         while j<=i:
#             if i%j==0:
#                 c=c+1
#             j=j+1
#         i=i+1
#     if c==2:
#         print("prime no.")
#     else:
#         print("not prime")
# n=int(input("enter the no."))
# add(n)


# 450 -> 145
# 960000 -> 96
# 1050 -> 105
# -1050 -> -105

# def add():
#     n=int(input("enter the no."))
#     rev=0
#     while n>0:
#         a=n%10
#         rev=rev*10+a
#         n=n//10
#     j=rev
#     b=0
#     while j>0:
#         a=j%10
#         b=b*10+a
#         j=j//10
#     print(b)
# add()

def add(n):
    rev=0
    while n>0:
        a=n%10
        rev=rev*10+a
        n=n//10
    j=rev
    b=0
    while j>0:
        a=j%10
        b=b*10+a
        j=j//10
    return b
n=int(input("enter the no."))
print(add(n))