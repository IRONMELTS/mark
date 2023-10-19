import csv

f1=open("mark.txt","r")
f2=open("marklist.csv","w",newline="")
w=csv.writer(f2)

c=0
cur_line=0

mark=[" "," "," "]
sub_codes={}
head=["roll no","sex","name"]

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


def enter_mark(roll,gender,name,sub_code_only,mark_only,grade_only,grade1,grade2,grade3,status):
    student_mark=mark.copy()
    student_mark[0]=roll
    student_mark[1]=gender
    student_mark[2]=name
    student_mark[-1]=status
    student_mark[-2]=grade3
    student_mark[-3]=grade2
    student_mark[-4]=grade1
    
    for i in sub_code_only:
        for j in sub_codes:
            if sub_codes[j]==int(i):
                student_mark[head.index(j)]=mark_only[sub_code_only.index(i)]
                student_mark[head.index(j)+1]=grade_only[sub_code_only.index(i)]
      
    w.writerow(student_mark)

no_sub=int(input("Enter no of subjects: "))

for i in range(no_sub):   
    sub=input("Enter subject name: ")
    code=int(input("Enter subject code: "))
    head.append(sub)
    head.append(f"{sub} grade")
    mark.append(" ")
    mark.append(" ")
    sub_codes[sub]=code

head.append("grade 1")
head.append("grade 2")
head.append("grade 3")
head.append("status")
mark.append(" ")
mark.append(" ")
mark.append(" ")
mark.append(" ")
    
lines=f1.readlines()
w.writerow(head)

for i in lines:
    cur_line+=1
    if i[0].isdigit():
        c+=1
        each_line=i.split()
        details=each_line
        m=details_thingy(details) #the line with roll no, name, sub code
        mark_grade=lines[cur_line].strip() #the line with the mark and grade
        n=mark_grade.split() #the real mark and grade

        sub_code_only=[]
        mark_only=[]
        grade_only=[]
        grade1=m[-4]
        grade2=m[-3]
        grade3=m[-2]
        status=m[-1]
        
        for k1 in m: #to get sub code only
            if k1.isdigit() and m.index(k1)!=0:
                sub_code_only.append(k1)
        for k2 in mark_grade.split(): #to get mark only
            if k2.isdigit():
                mark_only.append(k2)
        for k3 in mark_grade.split(): #to get grade only
            if k3.isalnum() and not k3.isdigit():
                grade_only.append(k3)

        enter_mark(m[0],m[1],m[2],sub_code_only,mark_only,grade_only,grade1,grade2,grade3,status)

                                      
print(f"Got mark of {c} students")
print("File has been created")
f1.close()
f2.close()
