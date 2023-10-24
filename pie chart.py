from openpyxl.workbook import Workbook
from openpyxl import load_workbook
import matplotlib.pyplot as plt
wb=load_workbook('marklist.xlsx')
ws=wb.active

#English
def pie_eng():
    plt.figure(figsize=(6,5))
    eng=ws['D']
    k=[]
    for i in eng:
        if not isinstance(i.value, str):
            k.append(i.value)

    acima90=0
    acima80=0
    acima60=0
    abaixo60=0
    l=['Above 90%','Above 80%','Above 60%','Belove 60%']
    for cell in k:
        if cell > 90:
            acima90+=1
        elif cell <=90 and cell > 80:
            acima80+=1
        elif cell <=80 and cell >60:
            acima60+=1
        else:
            abaixo60+=1
        
        
    val=[acima90,acima80,acima60,abaixo60]

    print(val)
    plt.pie(val,labels=l,autopct='%1.1f%%')
    plt.title('English')
    plt.show()

#Physics
def pie_phy():
    plt.figure(figsize=(6,5))
    phy=ws['F']
    k=[]
    for i in phy:
        if not isinstance(i.value, str):
            k.append(i.value)


    acima90=0
    acima80=0
    acima60=0
    abaixo60=0
    l=['Above 90%','Above 80%','Above 60%','Belove 60%']
    for cell in k:
        if cell > 90:
            acima90+=1
        elif cell <=90 and cell > 80:
            acima80+=1
        elif cell <=80 and cell >60:
            acima60+=1
        else:
            abaixo60+=1
            
            
    val=[acima90,acima80,acima60,abaixo60]

    print(val)
    plt.pie(val,labels=l,autopct='%1.1f%%')
    plt.title('Physics')
    plt.show()


#Chemistry
def pie_chem():
    plt.figure(figsize=(6,5))
    chem=ws['H']
    k=[]
    for i in chem:
        if not isinstance(i.value, str):
            k.append(i.value)


    acima90=0
    acima80=0
    acima60=0
    abaixo60=0
    l=['Above 90%','Above 80%','Above 60%','Belove 60%']
    for cell in k:
        if cell > 90:
            acima90+=1
        elif cell <=90 and cell > 80:
            acima80+=1
        elif cell <=80 and cell >60:
            acima60+=1
        else:
            abaixo60+=1
            
            
    val=[acima90,acima80,acima60,abaixo60]

    print(val)
    plt.pie(val,labels=l,autopct='%1.1f%%')
    plt.title('Chemistry')
    plt.show()

#Biology
def pie_bio():
    plt.figure(figsize=(6,5))
    bio=ws['J']
    k=[]
    for i in bio:
        if not isinstance(i.value, str):
            k.append(i.value)


    acima90=0
    acima80=0
    acima60=0
    abaixo60=0
    l=['Above 90%','Above 80%','Above 60%','Belove 60%']
    for cell in k:
        if cell > 90:
            acima90+=1
        elif cell <=90 and cell > 80:
            acima80+=1
        elif cell <=80 and cell >60:
            acima60+=1
        else:
            abaixo60+=1
            
            
    val=[acima90,acima80,acima60,abaixo60]

    print(val)
    plt.pie(val,labels=l,autopct='%1.1f%%')
    plt.title('Biology')
    plt.show()

    
#Maths
def pie_mat():
    plt.figure(figsize=(6,5))
    mat=ws['L']
    k=[]
    for i in mat:
        if not isinstance(i.value, str):
            k.append(i.value)


    acima90=0
    acima80=0
    acima60=0
    abaixo60=0
    l=['Above 90%','Above 80%','Above 60%','Belove 60%']
    for cell in k:
        if cell > 90:
            acima90+=1
        elif cell <=90 and cell > 80:
            acima80+=1
        elif cell <=80 and cell >60:
            acima60+=1
        else:
            abaixo60+=1
            
            
    val=[acima90,acima80,acima60,abaixo60]

    print(val)
    plt.pie(val,labels=l,autopct='%1.1f%%')
    plt.title('Maths')
    plt.show()

#Malayalam
def pie_mal():
    plt.figure(figsize=(6,5))
    mal=ws['N']
    k=[]
    for i in mal:
        if not isinstance(i.value, str):
            k.append(i.value)


    acima90=0
    acima80=0
    acima60=0
    abaixo60=0
    l=['Above 90%','Above 80%','Above 60%','Belove 60%']
    for cell in k:
        if cell > 90:
            acima90+=1
        elif cell <=90 and cell > 80:
            acima80+=1
        elif cell <=80 and cell >60:
            acima60+=1
        else:
            abaixo60+=1
            
            
    val=[acima90,acima80,acima60,abaixo60]

    print(val)
    plt.pie(val,labels=l,autopct='%1.1f%%')
    plt.title('Malayalam')
    plt.show()


#Hindi
def pie_hin():
    plt.figure(figsize=(6,5))
    hin=ws['P']
    k=[]
    for i in hin:
        if not isinstance(i.value, str):
            k.append(i.value)


    acima90=0
    acima80=0
    acima60=0
    abaixo60=0
    l=['Above 90%','Above 80%','Above 60%','Belove 60%']
    for cell in k:
        if cell > 90:
            acima90+=1
        elif cell <=90 and cell > 80:
            acima80+=1
        elif cell <=80 and cell >60:
            acima60+=1
        else:
            abaixo60+=1
            
            
    val=[acima90,acima80,acima60,abaixo60]

    print(val)
    plt.pie(val,labels=l,autopct='%1.1f%%')
    plt.title('Hindi')
    plt.show()
#Ecnomics
def pie_eco():
    plt.figure(figsize=(6,5))
    eco=ws['R']
    k=[]
    for i in eco:
        if not isinstance(i.value, str):
            k.append(i.value)


    acima90=0
    acima80=0
    acima60=0
    abaixo60=0
    l=['Above 90%','Above 80%','Above 60%','Belove 60%']
    for cell in k:
        if cell > 90:
            acima90+=1
        elif cell <=90 and cell > 80:
            acima80+=1
        elif cell <=80 and cell >60:
            acima60+=1
        else:
            abaixo60+=1
            
            
    val=[acima90,acima80,acima60,abaixo60]

    print(val)
    plt.pie(val,labels=l,autopct='%1.1f%%')
    plt.title('Ecnomics')
    plt.show()

#Computer
def pie_comp():
    plt.figure(figsize=(6,5))
    comp=ws['T']
    k=[]
    for i in comp:
        if not isinstance(i.value, str):
            k.append(i.value)


    acima90=0
    acima80=0
    acima60=0
    abaixo60=0
    l=['Above 90%','Above 80%','Above 60%','Belove 60%']
    for cell in k:
        if cell > 90:
            acima90+=1
        elif cell <=90 and cell > 80:
            acima80+=1
        elif cell <=80 and cell >60:
            acima60+=1
        else:
            abaixo60+=1
            
            
    val=[acima90,acima80,acima60,abaixo60]

    print(val)
    plt.pie(val,labels=l,autopct='%1.1f%%')
    plt.title('Computer')
    plt.show()

#Business
def pie_bus():
    plt.figure(figsize=(6,5))
    phy=ws['V']
    k=[]
    for i in phy:
        if not isinstance(i.value, str):
            k.append(i.value)


    acima90=0
    acima80=0
    acima60=0
    abaixo60=0
    l=['Above 90%','Above 80%','Above 60%','Belove 60%']
    for cell in k:
        if cell > 90:
            acima90+=1
        elif cell <=90 and cell > 80:
            acima80+=1
        elif cell <=80 and cell >60:
            acima60+=1
        else:
            abaixo60+=1
            
            
    val=[acima90,acima80,acima60,abaixo60]

    print(val)
    plt.pie(val,labels=l,autopct='%1.1f%%')
    plt.title('Business')
    plt.show()

#Accountancy
def pie_acc():
    plt.figure(figsize=(6,5))
    phy=ws['X']
    k=[]
    for i in phy:
        if not isinstance(i.value, str):
            k.append(i.value)


    acima90=0
    acima80=0
    acima60=0
    abaixo60=0
    l=['Above 90%','Above 80%','Above 60%','Belove 60%']
    for cell in k:
        if cell > 90:
            acima90+=1
        elif cell <=90 and cell > 80:
            acima80+=1
        elif cell <=80 and cell >60:
            acima60+=1
        else:
            abaixo60+=1
            
            
    val=[acima90,acima80,acima60,abaixo60]

    print(val)
    plt.pie(val,labels=l,autopct='%1.1f%%')
    plt.title('Accountancy')
    plt.show()
