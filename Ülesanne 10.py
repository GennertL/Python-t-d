#Ülesanne 10
#Gennert Lensment
#09.12.2020
import re
f = open("IP JA PAROOL.txt")
r = f.readlines()
for i in range(len(r)):
    if re.search("^((25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$", r[i]):
        print(r[i], end="")