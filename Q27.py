speed=int(input("enter the no."))
points=(speed-70)//5
if speed<70:
    print("ok")
elif speed>=70 and speed>130:
    print(points,"slow the car dangers ahead")
else:
   print(points,"suspend")


# list1=[1,10,2,3,5,7,1,-32,90,99,99]
# max=0
# secmax=0
# for i in list1:
#     if i>max:
#        max=i
# for i in list1:
#     if i>secmax and max!=i:
#       secmax=i
# print(secmax)


# l=[78,9,10,88]
# max=0
# secmax=0
# i=0
# while i<len(l):
#     if l[i]>max:
#         max=l[i]
#     i=i+1
# i=0
# while i<len(l):
#     if i>secmax and max!=i:
#         secmax=l[i]
#     i=i+1
# print(secmax)