class Circle:
 def __init__ (self, radio):
     self.radius = radio
 def circumference(self):
    pi = 3,14
    CircunferenceValue = pi * self.radius * 2
    return CircunferenceValue

 def PrintCircunferencia (self):
   myCircumference = self.circumference()
   print ("circuferencia del circulo con radio de " + str(self.radius) 
+ " es " + str(myCircumference))
# Primera instancia de la clase Circle.
circle1 = Circle(2)
circle2 = Circle(5)
circle3 = Circle(7)
# Llame a la PrintCircumference para la clase circle1 instanciada.
circle1.PrintCircunferencia()
# Dos instancias más y llamadas a métodos para la clase Circle.

circle2.PrintCircunferencia()

circle3.PrintCircunferencia()