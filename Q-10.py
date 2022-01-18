
# ###QQQQ-1 from meraki


# file=open("people1-exercise.txt","r")
# f=file.read()
# print(f)
# file.close()



# ###QQQQ-1 from meraki
# file=open("people1-exercise.txt","w")
# n=input("Enter the char\n")
# file.write(n)
# file.close()

file=open("people1-exercise.txt","r")
f=file.read()
i=0
c=1
while i<len(f):
    if "\n" in f[i]:
        c=c+1
    i=i+1
print(c,"total lines ")
file.close()