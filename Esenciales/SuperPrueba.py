#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
class Perros(object): #Declaramos la clase principal Perros
    def ladrar (self):
        print ("""Ladrido de Perro""")
        
    def grunir (self):
        print ("""Gruñido de Perro""")
class Caniche (Perros):#La clase secundaria hereda de la clase principal perros
    def ladrar(self):
        print ("""Ladrido de Caniche""")
        
    def grunir(self):
        print ("""Gruñido de Caniche""")

class Pastor_Aleman(Perros):#La clase secundaria hereda de la clase principal perros
    def ladrar(self):
        print ("""Ladrido de Pastor Aleman""")
        
    def grunir(self):
        print ("Gruñido de Pastor Aleman")
    
class Shepadoodle (Pastor_Aleman,Caniche):#La clase hereda de las clases hijas de su padre Perros
    def ladrarx(self, veces):
        for cuantas in range(veces):
            super(Shepadoodle, self).ladrar()

#Tommy = Pastor_Aleman()
#Piny = Caniche()
Cuchele = Shepadoodle()
Cuchele.ladrarx(5) # Imprime guau guau guau (5 veces) porque heredo el ladrido de la clase padre CANICHE
                    #Pero si eliminamos o renombramos el método ladrar de CANICHE que imprimiria?
                    #Imprimiria el ladrido del Pastor_Aleman
                    #Y  si borramos ambos? Imprimirá el ladrido de Perros!