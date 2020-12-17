# Gennert Lensment IT20
# 24.11.2020
#ülesanne 3

#Korralik nimi
nimi = int(input("Mis on teie nimi?:"))
tekst = ("Tere",nimi)
print(tekst.capitalize())

#Tundide ajad
algus = input("Sisesta algusaeg (hh:mm): ")
lõpp = input("Sisesta lõppaeg (hh:mm) ")
hh1, mm1 = algus.split(":")
hh2, mm2 = lõpp.split(":")
min1 = int(hh1)*60+(mm1)
min2 = int(hh2)*60+(mm2)
vahe = min2-min1
tund = vahe//60
minut = vahe%60
print(f"päeva pikkus on {tund}:{minut}: ")

#Email
email = input("Sisesta oma email: ")
print("@" in email)

#vandumine
lause = input("Ära siin vannu: ")
lause = (lause.lower()).replace("kurat","*****")
print(lause)

#korralik nimi
nimi = input("Sisesta nimi: ")
nimi =(nimi.strip()).nimi.capitalize()

print(nimi)