#Ülesanne 8
#Gennert Lensment
#09.12.2020

#klass
class Auto:
#atribuudid
    automark = 'puudub'
    aasta = 0
    hind = 0

#meetodid
    def __init__(self,x,y,z):
        self.automark = x
        self.aasta = y
        self.hind = z
    
    def lisaMark(self, x):
        self.automark = x
    
    def lisaAasta(self, x):
        self.aasta = x

    def lisaHind(self, x):
        self.hind = x
    
    def kuva(self):
        print(f"Automark: {self.automark} \nAasta {self.aasta} \hind: {self.hind}")
    
minuauto = Auto("honda", 2000, 10000)
    
minuauto.kuva()