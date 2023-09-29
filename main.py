f=open("mark.txt","r")
lines=f.readlines()
c=0
for i in lines:
    if i[0].isdigit():
        c+=1
        each_line=i.split()
        print(each_line)
print("Totally got: ",c)
f.close()
