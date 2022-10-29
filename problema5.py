elev1=("Gandac","Ion","Baiat",9,9,10)
elev2=("Costin","Ion","Baiat",7,8,4)
elev3=("Mateevici","Alexei","Baiat",6,8,4)
elev4=("Strutu","Catalina","Fata",6,9,8)
elev5=("Banana","Ioana","Fata",9,10,10)
elevi=[elev1,elev2,elev3,elev4,elev5]
print("\nLista elevilor:")
for elev in elevi:

    print(elev[0],elev[1],"are media:",round((elev[3]+elev[4]+elev[5])/3,2))
print("\nLista elevilor restantieri:")
for elev in elevi:
    if(elev[3]<5 or elev[4]<5 or elev[5]<5):
        print(elev[0],elev[1],"este restantier!")
print("\nLista elevilor eminenti:")
for elev in elevi:
    if(elev[3]>=9 and elev[4]>=9 and elev[5]>=9):
        print(elev[0],elev[1],"este eminent\\ă")
