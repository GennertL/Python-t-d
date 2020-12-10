#Murelikud lapsevanemad
kusimus = abs(int(input("Palun sisesta positiivse ringide arvu: ")))
print(kusimus)
i = 1
while i <= kusimus:
    print(i)
    i += 1
print(f"Jänku jooksis {i-1} ringi")

#äratus

äratustearv = int(input("Mitu korda tahad helinat? "))
for i in range(äratustearv):
    print("Tõuse ja sära!")

#Bussid

inimesed = int (input("kui mitu inimest?"))
kohad = int (input("mitu kohta on bussis?"))
if kohad > inimesed:
    print("vaja on 1 bussi")
else:
    
    if inimesed%kohad == 0:
        print("vaja on " + " " +str(inimesed//kohad) + " " + "bussi")
        print("viimases bussis on "+str(kohad))
    else:
        print("vaja on " + " " +str(inimesed//kohad+1) + " " + "bussi")
        print("viimases bussis on " +str(inimesed%kohad)+ " inimest")
#Pilved

kusimus = float(input("Mis on pilvede aluse kõrgus (kilomeetrites)?"))
if kusimus > 6:
    print("Need on ülemised pilved")
else:
    print("Need ei ole ülemised pilved")
                
#Aasta liblikas
aasta = 2020
liblikas = "teelehemosaiikliblikas"
lause_keskosa = ". aasta liblikas on "
lause = str(aasta) + lause_keskosa + liblikas
print(lause)

#Tervitus

print("Tere Maailm")