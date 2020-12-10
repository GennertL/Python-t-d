#Gennert LensmentIT20
#25.11.2020
#Ülessane 5

#õpilased
opilased = ['Juhan','Kati','Maarja','Mario','Mati']
print ("Vana nimekiri")
for i in range(len(opilased)):
    print(f"{i+1} {opilased[i]}")
arv = int(input("Mitmendat soovid muuta?"))
print(f"Valisid:{opilased[arv-1]}")

#lisab nime loendise
nimed = []

for i in range(5):
    nimi = input("Sisesta nimi:")
    nimed.append(nimi)
#näitab lisatud nime
print(nimi)
#sorterib nimed kasvavas järjestuses
nimed.sort()
print(nimed)
print("Viimati lisatud nimi: "),nimed


