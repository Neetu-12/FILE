# n=int(input("enter the no."))
# a=n//2*2
# if n==a:
#     print(n,"even no.")
# else:
#     print(n,"odd no.")


a=[[5,8,15,25],[4,28,45,2],[35,16,29]]
i=0
max=0
while i<len(a):
    j=0
    while j<len(a[i]):
        if a[i][j]>max:
            max=a[i]
        j=j+1
    i=i+1
print(max)