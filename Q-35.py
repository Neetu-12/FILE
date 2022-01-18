# age=int(input('enter the ages'))
# if age<=12:
#     print("kids drink the toddy")
# elif age>12 and age<=19:
#     print("teen age drink the coke")
# elif age>20 and age<=45:
#     print("adult drinks wisky")
# else:
#     print("can't drink ")


# a=[True,  True,  True,  False,
# True,  True,  True,  True ,
# True,  False, True,  False,
# True,  False, False, True ,
# True,  True,  True,  True ,
# False, False, True,  True]
# # i=0
# c1=0
# # c2=0
# while i<len(a):
#     if a[i]=='True':
#         c1=c1+1
#     elif a[i]=="False":
#         c2=c2+1
#     else:
#         pass
#     i=i+1
# print(c1)


# a=["i am neetu"]
# for i in a:
#     c=i.split(" ")
    # print(c)

# a=["i am neetu"]
# i=0
# while i<len(a):
#     j=0
#     while j<len(a[i]):
#         c=a[i].split(' ')
#         j=j+1
#     print(c)
#     i=i+1



# a=[[0], [1, 3], [5, 7], [9, 11], [13, 15, 17]]
# max=0
# i=0
# r=[]
# while i<len(a):
#     if len(a[i])>max:
#         max=len(a[i])
#         b=max
#         r.append(b)
#     print(r)
#     i=i+1
#     # print(r)
# print(max)
# # print(r)





# a=[[0], [1, 3], [5, 7], [9, 11], [13, 15, 17]]
# max=0
# i=0
# while i<len(a[i]):
#     if a[i]>max:
#         max=a[i]
#     i=i+1
# print(max)

a=[35,9,68,69,9]
i=0
max=0
sec_max=0
while i<len(a):
    if a[i]>max:
        sec_max=max
        max=a[i]
    if a[i]>sec_max and a[i]<max:
        sec_max=a[i]
    i=i+1
print(sec_max)