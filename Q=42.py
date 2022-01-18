# a=[12, 67, 98, 34]
# i=0
# r=[]
# while i<len(a):
#     j=0
#     while j<len(a):
#         s=s+a[i]+a[i]
#         r.append(s)
#         j=j+1
# #     i=i+1
# #     print(s)


# n=int(input("enter the no."))
# i=0
# while i<=n:
#     a=2**i
#     print(a)
#     i=i+1




# a=[12, 67, 98, 34]
# i=0
# r=[]
# while i<len(a):
#     n=a[i]
#     s=0
#     while n>0:
#         rem=n%10
#         s=s+rem
#         n=n//10
#     r.append(s)
#     i=i+1
# print(r)




a=[[5,6], [1,8, 3], [5, 7], [9, 11], [13, 15, 17]]
max=0
min=0
i=0
r=[]
while i<len(a):
    if len(a[i])>max:
        max=len(a[i])
        # r=a[i]
    i=i+1
min=max
j=0
while j<len(a):
    if len(a[j])<min:
        min=len(a[j])
        r=a[j]
    j=j+1
print(min,r)

