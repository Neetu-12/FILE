# n1=input("")
# n2=(n1)
# print(n2)

# # n2=input("enter the no.")
# # sum=n1+n2
# print(sum)

# a=8
# b=str(a)
# print(b)


# python2.7
# var1=(raw_input('enter the char'))
# var2=(raw_input('enter the char'))
# sum=var1+var2
# print(sum)


# n=int(input("enter the no"))
# a=n//2*2
# if n==a:
#     print("even")
# else:
#     print("odd ")


# num1 = 1
# def func():
#     num = num1 + 3
#     print(num)

# func()
# print(num1)

# a=[1450 ,960000, 1050 ,-1050]
# i=0
# r1=[]
# while i<len(a):
#     j=0
#     while j<len(a):
#         if a[i][j]=="0":
#             pass
#         else:
#             s=a[i][j]
#         j=j+1
#     r1.append(s)
#     i=i+1
# print(r1)


def add(n1,n2):
    a=int(n1)
    b=int(n2)
    s=a+b
    s1=str(s)
    print(type(s1))
    print(s1)
add("4","5")


a="python"
i=0
s=""
while i<len(a):
	s=s+a[i]
	i=i+1
	print(s)