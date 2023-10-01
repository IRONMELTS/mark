import csv

f1=open("mark.txt","r")
f2=open("test.csv","w",newline="")
w=csv.writer(f2)

lines=f1.readlines()
c=0
cur_line=0

for i in lines:
    cur_line+=1
    if i[0].isdigit():
        c+=1
        
        each_line=i.split()
        details=each_line
        mark_grade=lines[cur_line].strip()
        
        w.writerow(details)
        w.writerow(mark_grade.split())
        
print("Totally got: ",c)
print("File has been created")
f1.close()
f2.close()
