#Ülesanne 9
#Gennert Lensment
#09.12.2020

#Isikukoodist kuupäeva leidmine

ik = input("Sisesta isikukood: ")

#50403104211
if len(ik) == 11:
    p = ik[6:7]
    k = ik[4:5]
    a = ik[1:3]
    print(f"{p}.{k}. {a}")
    