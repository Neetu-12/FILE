# f = open("demofile.txt", "r")
# print(f.read())

# f = open("demofile.txt", "r")
# r=f.read()
# print(r)
# f.close()

# f = open("D:\\myfiles\welcome.txt", "r")
# print(f.read())



# f = open("demofile.txt", "r")
# for x in f:
#   print(x)


# f = open("demofile.txt", "r")
# print(f.readline())
# f = open("demofile.txt", "r")
# print(f.readline())
# f = open("demofile.txt", "r")
# print(f.readline())
# f.close()

f=open("demofile.txt", "r")
n=f.readlines()
print(n)
f=open("demofile.txt", "r")
n=f.readline()
print(n)
f.close()



f=open("demofile.txt", "r")
n=f.readline()
print(n)
f.close()