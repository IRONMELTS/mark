import csv

f1=open("mark.txt","r")
f2=open("marklist.csv","w",newline="")
mark=["  ","  ","  "," ","  "," ", "  ","  ","  ","  ","  ","  ","   "," ","  "," ", "  ","  ","  ","  ","  ","  ","   ","  ","  "]
w=csv.writer(f2)

lines=f1.readlines()
c=0

subject=["roll no","sex","name","301","grade","041","grade","042","grade","043","grade","044","grade","083","grade","112","grade","302","grade","030","grade","054","grade","055"]
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
w.writerow(subject)
for i in lines:
    cur_line+=1
    if i[0].isdigit():
        c+=1
        
        each_line=i.split()
        details=each_line
        
        
        m=details_thingy(details)
        
        mark_grade=lines[cur_line].strip()
        n=mark_grade.split()

        j=2     
        for e in range(0,len(n),2):
            mark[0]=m[0]
            mark[1]=m[1]
            mark[2]=m[2]
            j+=1
            if m[j]=="301":
                mark[3]=n[e]
                mark[4]=n[e+1]
            elif m[j]=="041":
                mark[5]=n[e]
                mark[6]=n[e+1]
            elif m[j]=="042":
                mark[7]=n[e]
                mark[8]=n[e+1]
            elif m[j]=="043":
                mark[9]=n[e]
                mark[10]=n[e+1]     
            elif m[j]=="044":
                mark[11]=n[e]
                mark[12]=n[e+1]
                
            elif m[j]=="083":
                mark[13]=n[e]
                mark[14]=n[e+1]
            elif m[j]=="112":
                mark[15]=n[e]
                mark[16]=n[e+1]
            elif m[j]=="302":
                mark[17]=n[e]
                mark[18]=n[e+1]
            elif m[j]=="030":
                mark[19]=n[e]
                mark[20]=n[e+1]
            elif m[j]=="054":
                mark[21]=n[e]
                mark[22]=n[e+1]
            elif m[j]=="055":
                mark[23]=n[e]
                mark[24]=n[e+1]
            
        w.writerow(mark)
        mark=[" ","  "," ", "  ","  ","  ","  ","  ","  ","   "," ","  "," ", "  ","  ","  ","  ","  ","  ","   ","  ","  ","  ","  "," "]



print("Totally got: ",c)
print("File has been created")
f1.close()
f2.close()
