# def add(n):
#     i=0
#     c1=0
#     c2=0
#     while i<len(l):
#         if l[i]>0:
#             c1=c1+1
#         if l[i]<0:
#             c2=c2+1
#         i=i+1
#     return (c1,"pos",c2,"neg")
# l = [2, -7, 5, -64, -14]
# print(add(l))



# def add():
#     n=int(input("enter the no."))
#     if n%3==0 and n%5==0:
#         print("fizz-buzz")
#     elif n%5==0:
#         print("buzz")
#     elif n%3==0:
#         print("fizz")
#     else:
#         print("both are equaal")
# add()

a=[3,4,6,9]
i=0
max=0
sec_max=0
while i<len(a):
    if a[i]>max:
        sec_max=max
    if a[i]<sec_max and max!=a[i]:
        max=a[i]
    i=i+1
print(sec_max)

# a=[3,4,6,9]
# i=0
# max=0
# while i<len(a):
#     if a[i]>max:
#         max=a[i]
#     i=i+1
# print(max)