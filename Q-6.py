# my_file2 = open("people2.txt", "r")
# d=my_file2.read()
# print(d)
# my_file2.close()

my_file2 = open("people2.txt", "r")
d=my_file2.read()
i=0
c=1
while i<len(d):
    if "\n" in d[i]:
        c+=1
    else:
        pass
    i+=1
print(c)
my_file2.close()


my_file3 = open("people3.txt", "w")
my_file3.write("Abhishek - Gurgaon\n")
my_file3.write("Ranveer - Delhi")
my_file3.close()