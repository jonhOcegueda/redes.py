class Location:
    #para crear el objeto se define el init que es un metodo especial
    def __init__(self,name,country) :
            self.name=name
            self.country=country
    #es un metodo y con el self llama los atributos ya antes enviados
    def MyLocation (self):
         print("Hi, my name is " + self.name + " and I live in " + 
self.country + ".")

#se crea el objeto o se instacia,que es lo mismo
loc=Location("jonh","mexico")
loc1=Location("pepe","portugal")
loc2=Location("andrea","nigeria")

loc1.MyLocation()
loc.MyLocation()
loc2.MyLocation()