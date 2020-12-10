#Gennert Lensment
#02.12.2020
#Ülesanne 6

#faili avamine
minu_fail = open('s6pru_l6ustaraamatus.txt', 'r')
ref = 0
ke = 0
erakondi_kokku = []
#faili sisu kuvamine
faili_sisu = minu_fail.readlines()
for i in range(len(faili_sisu)):
    #print(faili_sisu[i], end="")
    enimi, pnimi, ek, s = faili_sisu[i].split(" ")
    print(f"{enimi:11}{pnimi:11}{ek:5}{s:5}", end="")
    if ek == "RE":
        ref+=1
    if ek == "KE":
        ke+=1
    #Kui ei ole loendis...
    if ek not in erakondi_kokku:
        #... siis lisan loendisse
        erakondi_kokku.append(ek) 
    with open('uusfail.txt','a') as fail_kirjutamiseks:
        fail_kirjutamiseks.write(enimi+" "+pnimi+"\n")       
        
print("Reformikaid kokku:", ref)
print("Kesikuid kokku:", ke)
print("Erakondi kokku:", len(erakondi_kokku))

#Faili sulgemine
minu_fail.close()
