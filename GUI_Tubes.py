#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 27 12:55:15 2022

@author: antonio
"""

import tkinter as tk
import bloque as bk

class Gui_Tubes:
    
    def __init__(self, win):

        label1 = tk.Label(win, text="Number of tubes:")
        self.tn = tk.StringVar()
        tn_entry = tk.Entry(win, textvariable=self.tn)
        label21 = tk.Label(win, text="ud")

        label2 = tk.Label(win, text="Tubes thickness:")
        self.tt = tk.StringVar()
        tt_entry = tk.Entry(win, textvariable=self.tt)
        label22 = tk.Label(win, text="mm")

        label3 = tk.Label(win, text="Distance between tubes:")
        self.dbt = tk.StringVar()
        dbt_entry = tk.Entry(win, textvariable=self.dbt)
        label23 = tk.Label(win, text="mm")

        label4 = tk.Label(win, text="Tubes emmisivity:")
        self.em = tk.StringVar()
        em_entry = tk.Entry(win, textvariable=self.em)
        label24 = tk.Label(win, text="p.u.")


        label1.grid(column=0, row=0, sticky="E")
        tn_entry.grid(column=1, row=0, sticky="WE")
        label21.grid(column=2, row=0, sticky="W")

        label2.grid(column=0, row=1, sticky="E")
        tt_entry.grid(column=1, row=1, sticky="WE")
        label22.grid(column=2, row=1, sticky="W")

        label3.grid(column=0, row=2, sticky="E")
        dbt_entry.grid(column=1, row=2, sticky="WE")
        label23.grid(column=2, row=2, sticky="W")

        label4.grid(column=0, row=3, sticky="E")
        em_entry.grid(column=1, row=3, sticky="WE")
        label24.grid(column=2, row=3, sticky="W")

    def newData(self):
        self.tn.set("")
        self.tt.set("")
        self.dbt.set("")
        self.em.set("")

    def getData(self):
        lista = list()
        lista.append(self.tn.get())
        lista.append(self.tt.get())
        lista.append(self.dbt.get())
        lista.append(self.em.get())
        return lista
    
    def setData(self, lista):
        self.tn.set(lista[0])
        self.tt.set(lista[1])
        self.dbt.set(lista[2])
        self.em.set(lista[3])
                
    def createBlock(self):
        
        numEspBlk = float(self.tnt.get()) / (float(self.cchn.get()) + 1.0)
        numEspAccum = 0.0
        numEspBlkInicio = 0
        numEspBlkFin = 0
        
        radialTotal =(float(self.iit.get()) + 
                      float(self.tnt.get()) * (float(self.cw.get()) + float(self.ibt.get())) +
                      float(self.cchn.get()) * float(self.ccht.get()) +
                      float(self.oit.get()))
        diamMedMecaTotal = (float(self.dim.get()) + radialTotal) / 1000.0
        diamMedElecTotal = (float(self.dim.get()) +
                            2 * float(self.iit.get()) + radialTotal -
                            float(self.oit.get())) / 1000.0
        radialTotal = radialTotal / 1000.0
       
        for n in range(int(self.cchn.get()) + 1):
            bl = bk.Bloque()
            
            bk.contadorBloques = bk.contadorBloques + 1
            bl.nInd = bk.contadorBloques
            
            bl.tAmb = 273.0 + 20.0
            
            bl.diamInt = (float(self.dim.get()) +
                          float(self.iit.get()) +
                          numEspBlkFin * (float(self.cw.get()) + float(self.ibt.get())) +
                          n * int(self.ccht.get())) / 1000.0
            
            numEspBlkFin = round(numEspAccum + numEspBlk)
            
            bl.diamExt = (float(self.dim.get()) +
                          float(self.iit.get()) +
                          numEspBlkFin * (float(self.cw.get()) + float(self.ibt.get())) +
                          n * int(self.ccht.get())) / 1000.0
            
            diamMedElec = (bl.diamInt + bl.diamExt) / 2.0
            
            if n == 0:
                bl.diamInt = bl.diamInt - float(self.iit.get()) / 1000.0
            if n == int(self.cchn.get()):
                bl.diamExt = bl.diamExt + float(self.oit.get()) / 1000.0
            diamMedMeca = (bl.diamInt + bl.diamExt) / 2.0
            
            bl.alt = float(self.ch.get()) / 1000.0
            bl.areaInt = 3.141592 * bl.diamInt * bl.alt
            bl.areaExt = 3.141592 * bl.diamExt * bl.alt
            
            bl.emisiv = float(self.em.get())
            
            a = diamMedElec / diamMedElecTotal
            a = a * (numEspBlkFin - numEspBlkInicio) / float(self.tnt.get())
            b = diamMedMeca / diamMedMecaTotal
            b = b * (bl.diamExt - bl.diamExt) / radialTotal
            
            bl.pesoFe = 0.0
            if self.cm.get() == "Cu":
                bl.pesoCu = a * float(self.cbw.get()) / 3.0
            else:
                bl.pesoAl = a * float(self.cbw.get()) / 3.0
            bl.pesoAisl = b * (float(self.tww.get()) - float(self.cbw.get())) / 3.0
            
            if losses:
                bl.pkOhm = a * float(self.wol.get()) / 3.0
                bl.pkAdi = a * float(self.wol.get()) / 3.0
            
            bl.tRef = float(self.rt.get())
            bl.temp = 273.0 + 20.0
            bl.incTemp = 1000.0
            
            bl.pk = 0.0
            bl.pConv = 0.0
            bl.pRad = 0.0
            
            bl.velAirInt = float(self.aiv.get())
            bl.velAirChn = float(self.acchv.get())
            bl.velAirExt = float(self.aev.get())

            numEspBlkInicio = numEspBlkFin + 1
            numEspAccum = numEspAccum + numEspBlk
                    
            bk.bloques.append(bl)
