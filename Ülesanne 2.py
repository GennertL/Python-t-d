# Gennert Lensment
# 20.11.2020
# Ülesanne 2

#Arvutame kolmnurga ümbermõõdi
a,b,c = 2,3,4
p = a+b+c
print("Kolmnurga ümbermõõt on",p)

#Toote hind
hind, ale, kogus = 36.75, 0.4, 3
summa = (hind-hind*ale)*kogus,
print(kogus, "toote summa on",summa,"€")

#Pitsa
hind, tip = 12.90, 0.10
tip = 12.90 * 0.10
inimesi = 3
kokku = hind + tip
maksmine = kokku/inimesi
print("Inimesed pidid kokku maksma",maksmine,"€")
#Kaugele jõuab rulluisutaja
kiirus = 29.9
aeg = 24/60
distants = kiirus*aeg
print("Rulluisutaja jõudis 24 minutiga",distants,"km kaugusele")

#Kolmnurga hüpotenuus
külg1, külg2 = 16, 9
külg3 = külg1**2 + külg2**2
import math
ruutjuur = math.sqrt(külg3) 
print("Hüpotenuus on",ruutjuur,)

#Ajateisendus
aeg = int(input("Sisesta aeg minutites: "))
h = aeg//60
m = aeg%60
p = "Pole oluline muutuja"
print(aeg,"minutit on",h,":",m)

#Arvusüsteemid
arv = int(input("Sisesta täisarv 10ndsüsteemis:"))
kahend = bin(arv)
kuusteist = hex(arv)
print("2ndsüsteemi arv:",kahend,)
print("16ndsüsteemi arv:",kuusteist,)

#Kütusekulu arvutamine
tangitud = int(input("Sisesta tangitud kütuse liitrid:"))
läbitud = int(input("Sisesta läbitud kilomeetrid:"))
km = läbitud
kütus = tangitud / (km / 100)
print("kütusekulu on",kütus,)
