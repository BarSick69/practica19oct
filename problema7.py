om1=("Gandac","Ion",17,179,110,"Baiat","casatorit")
om2=("Costin","Ion",17,188,45,"Baiat","necasatorit")
om3=("Strutu","Catalina",29,169,78,"Fata","casatorit")
om4=("Banana","Ioana",21,180,120,"Fata","necasatorit")
oameni=[om1,om2,om3,om4]
nr=len(oameni)
v=0
i=0
m=0
nr_mm_18=0
nr_de_fete=0
fem_necasatorite=0
pers_grase=0
for om in oameni:
    if(om[2]<20):
        v+=1
    if(om[3]>170):
        i+=1
    if(om[2]>18):
        nr_mm_18+=1
        m+=om[4]
    if(om[5]=="Fata"):
        nr_de_fete+=1
    if(om[5]=="Fata" and om[2]>20 and om[6]=="necasatorit"):
        fem_necasatorite+=1
    
    

v=(v/nr)*100
i=(i/nr)*100
if(nr_mm_18>=1):
    m_medie=m/nr_mm_18
if(nr_de_fete!=0):
    fem_necasatorite=(fem_necasatorite/nr_de_fete)*100
for om in oameni:
    if(om[2]>20 and om[2]<50 and om[4]>m_medie):
        pers_grase+=1
    pers_grase=(pers_grase/nr)*100



print("Persoane sub 20 ani:",v,'%')
print("Persoane cu inaltimea m.m de 170cm:",i,'%')
print("Masa medie a unei persoane de peste 18 ani:",m_medie)
print("Procentul persoanelor de sex feminin ce au peste 20 de ani și nu sunt căsătorite:",fem_necasatorite,'%')
print("ce procent din numărul persoanelor între 20 și 50 ani au greutatea mai mare decât greutatea medie:",pers_grase,'%')

