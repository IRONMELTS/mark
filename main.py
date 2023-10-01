import csv

f1=open("mark.txt","r")
f2=open("test.csv","w",newline="")
w=csv.writer(f2)

lines=f1.readlines()
c=0
cur_line=0

def details_thingy(a):
    l=[]
    l.append(a[0])
    l.append(a[1])
    
    go=True
    c=0
    name=""
    
    for i in range(2,len(a)):
        if go==True and a[i].isdigit()==False:
            name=(f" {name} {a[i]} ")
        elif go==False:
            l.append(str(a[i]))
        elif a[i].isdigit()==True:
            go=False
            l.append(str(a[i]))
        if c==0 and go==False:
            c+=1
            l.append(name.strip())
    l[2],l[3]=l[3],l[2]
    return l

for i in lines:
    cur_line+=1
    if i[0].isdigit():
        c+=1
        
        each_line=i.split()
        details=each_line
        mark_grade=lines[cur_line].strip()
        
        w.writerow(details_thingy(details))
        w.writerow(mark_grade.split())
        
print("Totally got: ",c)
print("File has been created")
f1.close()
f2.close()
