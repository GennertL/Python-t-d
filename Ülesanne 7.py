#Gennert Lensment
#02.12.2020
#Ülesanne 6

#Ruulama leidmine

def kuup():
    return "Kuubi arvutamine"

def kere():
    return "Kera leidmine"

def koonus():
    return "koonuse leidmine"

def silinder():
    return "Silindri leidmine"



loop = 1
while loop==1:
    print("Tee valik")
    print("1. Kuup")
    print("2. Kera")
    print("3.Koonus")
    print("4. Silinder")
    print()
    valik = int(input("Tee valik 1-4; "))
    if valik==1:
        print(kuup())





#Tervitus
def tervita(keel="ger"):
    'tervitus'
    keel = input("Wähle eine Sprache eng/est/ger:")
    if keel=="eng":
        nimi = input("enter a name")
        return("Hello " + nimi) 
    
    if keel=="est":
        nimi = input("Sisesta nimi")
        return("tere " + nimi)
    else:
        nimi = input("Geben Sie einen Namen ein")
        return("Hallo " +nimi)
    
    
      
      
print(tervita())