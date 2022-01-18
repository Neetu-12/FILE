
# def max_of_two( x, y ):
#     if x > y:
#         return x
#     return y
# def max_of_three( x, y, z ):
#     return max_of_two( x, max_of_two( y, z ) )
# print(max_of_three(3, 6, -5))

# string="1234abcd"
# s=""
# i=len(string)
# while i>0:
#     s=s+string[i-1]
#     i=i-1
# print(s)


# n=input("enter th char")
# i=-1
# s=""
# while i>=-len(n):
#     s=s+n[i]
#     i=i-1
# if s==n:
#     print("pallindrome")
# else:
#     print("not a pallindrome")

n=int(input("enter the no."))
if n%3==0:
    print("fizz")
elif n%5==0:
    print("buzz")
elif n%3==0 and n%5==0:
    print("fizz-buzz")
else:
  print("both are equaal")