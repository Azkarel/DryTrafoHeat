# -*- coding: utf-8 -*-
"""
Created on Tue Oct 11 13:04:10 2022

@author: antonio
"""
from tkinter import filedialog
import math
import csv

import air

#  Se crea una lista llamada bloques de objetos de la clase bloque
bloques = []
contadorBloques = 0

class Bloque(object):
    
    def __init__(self):
        self.nInd = 0
        self.tAmb = 0.0
        self.diamInt = 0.0
        self.diamExt = 0.0
        self.alt = 0.0
        self.areaInt = 0.0
        self.areaExt = 0.0
        self.emisiv = 0.0
        self.pesoFe = 0.0
        self.pesoAl = 0.0
        self.pesoCu = 0.0
        self.pesoAisl = 0.0
        self.pkOhm = 0.0
        self.pkAdi = 0.0
        self.tRef = 0.0
        self.temp = 0.0
        self.incTemp = 0.0
        self.pk = 0.0
        self.pConv = 0.0
        self.pRad = 0.0
        self.velAirInt = 0.0
        self.velAirChn = 0.0
        self.velAirExt = 0.0


    #  Calculo de las perdidas disipadas por conveccion en AN
    #########################################################
    
    def perdidasConveccionAN(self):
        
        #  Calculo del coeficiente de transmisión de calor de la sup. int.
        if self.nInd > 0:
            
            nusselt = air.ANnusseltChannel2side(self.tAmb, self.temp,
                                          bloques[self.nInd-1].diamExt, 
                                          self.diamInt, 
                                          self.alt)
            
            s = (0.5 * math.sqrt(bloques[self.nInd-1].diamExt * self.diamInt) 
                 * math.log(self.diamInt / bloques[self.nInd-1].diamExt))

        else:
            
#            nusselt = air.ANnusseltChannel2side(self.tAmb, self.temp,
#                                          10.0, 10.0 + self.diamInt, self.alt)
            
            nusselt = 0
            s = 10

        alfaInt = (nusselt * air.lamb((self.tAmb + self.temp) / 2)) / s

        #  Calculo de perdidas disipadas por convección interiores        
        pConvInt = alfaInt * (self.temp - self.tAmb) * self.areaInt
        
        #  Calculo del coeficiente de transmisión de calor de la sup. ext.
        if self.nInd < (len(bloques)-1):
            
            nusselt = air.ANnusseltChannel2side(self.tAmb, self.temp,
                                          self.diamExt, 
                                          bloques[self.nInd+1].diamInt, 
                                          self.alt)
            
            s = (0.5 * math.sqrt(self.diamExt * bloques[self.nInd+1].diamInt)  
                 * math.log(bloques[self.nInd+1].diamInt / self.diamExt))

        else:
            
            nusselt = air.ANnusseltWall(self.tAmb, self.temp, self.alt)
            
            s = self.alt

        alfaExt = (nusselt * air.lamb((self.tAmb + self.temp) / 2)) / s
        
        #  Calculo de perdidas disipadas por convección exteriores        
        pConvExt = alfaExt * (self.temp - self.tAmb) * self.areaExt
        
        return(pConvInt + pConvExt)

        
    #  Calculo de las perdidas disipadas por conveccion en AF
    #########################################################
    
    def perdidasConveccionAF(self):
        
        #  Calculo del coeficiente de transmisión de calor de la sup. int.
        if self.nInd > 0:
                    
            nusselt = air.AFnusseltChannel(self.tAmb, self.temp,
                                           bloques[self.nInd-1].diamExt, 
                                           self.diamInt, 
                                           self.alt,
                                           self.velAirInt)
            
            dh = self.diamInt - bloques[self.nInd-1].diamExt
            
        else:
            
#            nusselt = air.AFnusseltChannel(self.tAmb, self.temp,
#                                          10.0,
#                                          10.0 + self.diamInt, 
#                                          self.alt,
#                                          self.velAirInt)
            nusselt = 0  
            dh = 10
          
        alfaInt = (nusselt * air.lamb((self.tAmb + self.temp) / 2)) / dh

        #  Calculo de perdidas disipadas por convección interiores        
        pConvInt = alfaInt * (self.temp - self.tAmb) * self.areaInt
        
        #  Calculo del coeficiente de transmisión de calor de la sup. ext.
        if self.nInd < (len(bloques)-1):
            
            nusselt = air.AFnusseltChannel(self.tAmb, self.temp,
                                          self.diamExt, 
                                          bloques[self.nInd+1].diamInt, 
                                          self.alt,
                                          self.velAirExt)
            
            dh =  bloques[self.nInd+1].diamInt - self.diamExt

        else:
            
            nusselt = air.AFnusseltWall(self.tAmb, self.temp, 
                                        self.alt,
                                        self.velAirExt)
            dh = self.alt
            
        alfaExt = (nusselt * air.lamb((self.tAmb + self.temp) / 2)) / dh
        
        #  Calculo de perdidas disipadas por convección exteriores        
        pConvExt = alfaExt * (self.temp - self.tAmb) * self.areaExt
        
        return(pConvInt + pConvExt)

        
    #  Calculo de las perdidas disipadas por radiación        
    ##################################################
    
    def perdidasRadiacion(self):
        
        stefan_boltzmann = 5.6704e-8
        
        #  Calculo del coeficiente de transmisión de calor de la sup. int.
        if self.nInd > 0:
            
            a1 = bloques[self.nInd-1].areaExt
            a2 = self.areaInt
            e1 = bloques[self.nInd-1].emisiv
            e2 = self.emisiv
            c21 = stefan_boltzmann / ((1 / e2) + (a2 / a1) * ((1 / e1) + 1))
            
            pRadInt = c21 * (self.temp ** 4.0 - 
                             bloques[self.nInd-1].temp ** 4.0)   
            
        else:
            
            pRadInt = 0  # El nucleo no tiene radiación interior
            
        #  Calculo del coeficiente de transmisión de calor de la sup. ext.
        if self.nInd < (len(bloques)-1):
            
            a1 = bloques[self.nInd+1].areaInt
            a2 = self.areaExt
            e1 = bloques[self.nInd+1].emisiv
            e2 = self.emisiv
            c21 = stefan_boltzmann / ((1 / e2) + (a2 / a1) * ((1 / e1) + 1))
            
            pRadExt = c21 * (self.temp ** 4.0 - 
                             bloques[self.nInd+1].temp ** 4.0)
            
        else:
            
            pRadExt = (stefan_boltzmann * self.emisiv * self.areaExt * 
                       (self.temp ** 4 - self.tAmb ** 4))
        
        return(pRadInt + pRadExt)
    
    
    #  Calculo del incremento de temperatura del bloque después de s segundos
    #########################################################################
    
    def actualizaTemp(self, regimen, s):
        
        #  Corrección de las perdidas del bloque con su temperatura
        if self.pesoAl > 0 and self.pesoCu < 0.1:
            constCriogenica = 235.0
        elif self.pesoAl < 0.1 and self.pesoCu > 0:
            constCriogenica = 225.0
        elif self.pesoAl > 0 and self.pesoCu > 0:
            constCriogenica = 230.0
        else:
            constCriogenica = 1.0e99  # se supone que es el nucleo 
            
        self.pk = self.pkOhm * ((constCriogenica + self.temp) / 
                           (constCriogenica + self.tRef))
        self.pk += self.pkAdi * ((constCriogenica + self.tRef) / 
                            (constCriogenica + self.temp))
        
        #  Calculo de las perdidas disipadas
        if regimen == "AN":
            self.pConv = self.perdidasConveccionAN()
        else:
            self.pConv = self.perdidasConveccionAF()
            
        self.pRad = self.perdidasRadiacion()
        
        #  Calculo de las perdidas que calentaran el bloque
        pInternas = self.pk - self.pConv - self.pRad
        
        #  Calculo del calor especifico del bloque
        calorEspecif = (self.pesoFe * 450 +
                        self.pesoAl * 900 +
                        self.pesoCu * 385 +
                        self.pesoAisl * 1470)
        
        self.incTemp = s * pInternas / calorEspecif
        
        
# Guarda los bloques en un fichero csv
######################################
    
def guardaBloques():
    
    filename = filedialog.asksaveasfilename(defaultextension=".blk", filetypes=[("bloques", ".blk")])

    with open(filename, "w", newline='') as csv_file:
        csv_writer = csv.writer(csv_file, dialect="excel")
        
        for bl in bloques:
            
            lista = list()
            lista.append(bl.nInd)
            lista.append(bl.tAmb)
            lista.append(bl.diamInt)
            lista.append(bl.diamExt) 
            lista.append(bl.alt) 
            lista.append(bl.areaInt) 
            lista.append(bl.areaExt) 
            lista.append(bl.emisiv) 
            lista.append(bl.pesoFe) 
            lista.append(bl.pesoAl) 
            lista.append(bl.pesoCu)
            lista.append(bl.pesoAisl)
            lista.append(bl.pkOhm)
            lista.append(bl.pkAdi)
            lista.append(bl.tRef)
            lista.append(bl.temp)
            lista.append(bl.incTemp)
            lista.append(bl.pk)
            lista.append(bl.pConv)
            lista.append(bl.pRad)
            lista.append(bl.velAirInt)
            lista.append(bl.velAirChn)
            lista.append(bl.velAirExt)
            
            csv_writer.writerow(lista)

        