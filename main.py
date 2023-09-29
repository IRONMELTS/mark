f=open("mark.txt","r")
lines=f.readlines()
c=0
cur_line=0

for i in lines:
    cur_line+=1
    if i[0].isdigit():
        c+=1
        each_line=i.split()
        details=each_line
        mark_grade=lines[cur_line]
        print(details)
        print(mark_grade.strip())

print("Totally got: ",c)
f.close()
