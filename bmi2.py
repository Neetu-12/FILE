# bmi=int(input("enter the no."))
# if bmi <= 18.5 return "Underweight"
# if bmi <= 25.0 return "Normal"
# if bmi <= 30.0 return "Overweight"
# if bmi > 30 return "Obese"



# l='The quick Brow Fox'
# i=0
# c1=0
# c2=0
# while i<len(l):
#     if l[i]>"A" and l[i]<="Z":
#         c1=c1+1
#     elif l[i]>"a" and l[i]<="z":
#         c2=c2+1
#     else:
#         pass
#     i=i+1
# print("capital latter",c1)
# print("small letter",c2)


# def increment():
#     def inner(num):
#         print(num+1)
#     return inner(90)
# increment()


# def increment(num):
#     def inner():
#         print(increment(num+1))
#     return inner()
# increment(90)


# def add(a):
#     underweight=a
#     return underweight
# def sub(b):
#     normal=b
#     return normal
# def mult(d):
#     overweight=d
#     return overweight
# def div(e):
#     obese=e
#     return obese
# def main():
#     if bmi<=18.5:
#         print(add(bmi))
#     elif bmi<=25.0:
#         print(sub(bmi))
#     elif bmi<=30.0:
#         print(mult(bmi))
#     elif bmi>30:
#         print(div(bmi))
# weight=int(input("enter your weight"))
# height2=int(input("enter your height2"))
# bmi=weight//height2
# main()


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

