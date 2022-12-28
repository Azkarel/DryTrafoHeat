#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 27 12:55:15 2022

@author: antonio
"""

import tkinter as tk
import bloque as bk

class Gui_Foil:
    
    def __init__(self, win):

        label0 = tk.Label(win, text="Total number of turns:")
        self.tnt = tk.StringVar()
        tnt_entry = tk.Entry(win, textvariable=self.tnt)
        label20 = tk.Label(win, text="ud")

        label1 = tk.Label(win, text="Mechanical interior diameter:")
        self.dim = tk.StringVar()
        dim_entry = tk.Entry(win, textvariable=self.dim)
        label21 = tk.Label(win, text="mm")

        label2 = tk.Label(win, text="Conductor height:")
        self.ch = tk.StringVar()
        ch_entry = tk.Entry(win, textvariable=self.ch)
        label22 = tk.Label(win, text="mm")

        label3 = tk.Label(win, text="Conductor thickness:")
        self.cw = tk.StringVar()
        cw_entry = tk.Entry(win, textvariable=self.cw)
        label23 = tk.Label(win, text="mm")

        label4 = tk.Label(win, text="Insulation between turns thickness:")
        self.ibt = tk.StringVar()
        ibt_entry = tk.Entry(win, textvariable=self.ibt)
        label24 = tk.Label(win, text="mm")

        label5 = tk.Label(win, text="Inner insulation thickness:")
        self.iit = tk.StringVar()
        iit_entry = tk.Entry(win, textvariable=self.iit)
        label25 = tk.Label(win, text="mm")

        label6 = tk.Label(win, text="Outer insulation thickness:")
        self.oit = tk.StringVar()
        oit_entry = tk.Entry(win, textvariable=self.oit)
        label26 = tk.Label(win, text="mm")

        label7 = tk.Label(win, text="Cooling channel number:")
        self.cchn = tk.StringVar()
        cchn_entry = tk.Entry(win, textvariable=self.cchn)
        label27 = tk.Label(win, text="ud")

        label8 = tk.Label(win, text="Cooling channel thickness:")
        self.ccht = tk.StringVar()
        ccht_entry = tk.Entry(win, textvariable=self.ccht)
        label28 = tk.Label(win, text="mm")

        label9 = tk.Label(win, text="Total weight of 3 coils:")
        self.tww = tk.StringVar()
        tww_entry = tk.Entry(win, textvariable=self.tww)
        label29 = tk.Label(win, text="kg")

        label10 = tk.Label(win, text="Conductor Material:")
        self.cm = tk.StringVar()
        cm_entry = tk.Entry(win, textvariable=self.cm)
        label30 = tk.Label(win, text="Al / Cu")

        label11 = tk.Label(win, text="Conductor+Busbars weight:")
        self.cbw = tk.StringVar()
        cbw_entry = tk.Entry(win, textvariable=self.cbw)
        label31 = tk.Label(win, text="kg")

        label12 = tk.Label(win, text="Winding ohmic losses:")
        self.wol = tk.StringVar()
        wol_entry = tk.Entry(win, textvariable=self.wol)
        label32 = tk.Label(win, text="W")

        label13 = tk.Label(win, text="Winding eddy losses:")
        self.wel = tk.StringVar()
        wel_entry = tk.Entry(win, textvariable=self.wel)
        label33 = tk.Label(win, text="W")

        label14 = tk.Label(win, text="Reference temperature")
        self.rt = tk.StringVar()
        rt_entry = tk.Entry(win, textvariable=self.rt)
        label34 = tk.Label(win, text="ºC")

        label15 = tk.Label(win, text="Winding emissivity:")
        self.em = tk.StringVar()
        em_entry = tk.Entry(win, textvariable=self.em)
        label35 = tk.Label(win, text="p.u.")

        label16 = tk.Label(win, text="Inner air velocity:")
        self.aiv = tk.StringVar()
        aiv_entry = tk.Entry(win, textvariable=self.aiv)
        label36 = tk.Label(win, text="m/s")

        label17 = tk.Label(win, text="Cooling channel air velocity:")
        self.acchv = tk.StringVar()
        acchv_entry = tk.Entry(win, textvariable=self.acchv)
        label37 = tk.Label(win, text="m/s")

        label18 = tk.Label(win, text="Outer side air velocity:")
        self.aev = tk.StringVar()
        aev_entry = tk.Entry(win, textvariable=self.aev)
        label38 = tk.Label(win, text="m/s")
        
        
        label0.grid(column=0, row=0, sticky="E")
        tnt_entry.grid(column=1, row=0, sticky="WE")
        label20.grid(column=2, row=0, sticky="W")
        
        label1.grid(column=0, row=1, sticky="E")
        dim_entry.grid(column=1, row=1, sticky="WE")
        label21.grid(column=2, row=1, sticky="W")
       
        label2.grid(column=0, row=2, sticky="E")
        ch_entry.grid(column=1, row=2, sticky="WE")
        label22.grid(column=2, row=2, sticky="W")

        label3.grid(column=0, row=3, sticky="E")
        cw_entry.grid(column=1, row=3, sticky="WE")
        label23.grid(column=2, row=3, sticky="W")

        label4.grid(column=0, row=4, sticky="E")
        ibt_entry.grid(column=1, row=4, sticky="WE")
        label24.grid(column=2, row=4, sticky="W")

        label5.grid(column=0, row=5, sticky="E")
        iit_entry.grid(column=1, row=5, sticky="WE")
        label25.grid(column=2, row=5, sticky="W")

        label6.grid(column=0, row=6, sticky="E")
        oit_entry.grid(column=1, row=6, sticky="WE")
        label26.grid(column=2, row=6, sticky="W")

        label7.grid(column=0, row=7, sticky="E")
        cchn_entry.grid(column=1, row=7, sticky="WE")
        label27.grid(column=2, row=7, sticky="W")

        label8.grid(column=0, row=8, sticky="E")
        ccht_entry.grid(column=1, row=8, sticky="WE")
        label28.grid(column=2, row=8, sticky="W")
        
        label9.grid(column=0, row=9, sticky="E")
        tww_entry.grid(column=1, row=9, sticky="WE")
        label29.grid(column=2, row=9, sticky="W")        
        
        label10.grid(column=0, row=10, sticky="E")
        cm_entry.grid(column=1, row=10, sticky="WE")
        label30.grid(column=2, row=10, sticky="W")
        
        label11.grid(column=0, row=11, sticky="E")
        cbw_entry.grid(column=1, row=11, sticky="WE")
        label31.grid(column=2, row=11, sticky="W")
        
        label12.grid(column=0, row=12, sticky="E")
        wol_entry.grid(column=1, row=12, sticky="WE")
        label32.grid(column=2, row=12, sticky="W")
        
        label13.grid(column=0, row=13, sticky="E")
        wel_entry.grid(column=1, row=13, sticky="WE")
        label33.grid(column=2, row=13, sticky="W")
        
        label14.grid(column=0, row=14, sticky="E")
        rt_entry.grid(column=1, row=14, sticky="WE")
        label34.grid(column=2, row=14, sticky="W")
        
        label15.grid(column=0, row=15, sticky="E")
        em_entry.grid(column=1, row=15, sticky="WE")
        label35.grid(column=2, row=15, sticky="W")
        
        label16.grid(column=0, row=16, sticky="E")
        aiv_entry.grid(column=1, row=16, sticky="WE")
        label36.grid(column=2, row=16, sticky="W")
        
        label17.grid(column=0, row=17, sticky="E")
        acchv_entry.grid(column=1, row=17, sticky="WE")
        label37.grid(column=2, row=17, sticky="W")
        
        label18.grid(column=0, row=18, sticky="E")
        aev_entry.grid(column=1, row=18, sticky="WE")
        label38.grid(column=2, row=18, sticky="W")

    def newData(self):
        self.tnt.set("")
        self.dim.set("")
        self.ch.set("")
        self.cw.set("")
        self.ibt.set("")
        self.iit.set("")
        self.oit.set("")
        self.cchn.set("")
        self.ccht.set("")
        self.tww.set("")
        self.cm.set("")
        self.cbw.set("")
        self.wol.set("")
        self.wel.set("")
        self.rt.set("")
        self.em.set("")
        self.aiv.set("")
        self.acchv.set("")
        self.aev.set("")

        
    def getData(self):
        lista = list()
        lista.append(self.tnt.get())
        lista.append(self.dim.get())
        lista.append(self.ch.get())
        lista.append(self.cw.get())
        lista.append(self.ibt.get())
        lista.append(self.iit.get())
        lista.append(self.oit.get())
        lista.append(self.cchn.get())
        lista.append(self.ccht.get())
        lista.append(self.tww.get())
        lista.append(self.cm.get())
        lista.append(self.cbw.get())
        lista.append(self.wol.get())
        lista.append(self.wel.get())
        lista.append(self.rt.get())
        lista.append(self.em.get())
        lista.append(self.aiv.get())
        lista.append(self.acchv.get())
        lista.append(self.aev.get())
        return lista
    
    def setData(self, lista):
        self.tnt.set(lista[0])
        self.dim.set(lista[1])
        self.ch.set(lista[2])
        self.cw.set(lista[3])
        self.ibt.set(lista[4])
        self.iit.set(lista[5])
        self.oit.set(lista[6])
        self.cchn.set(lista[7])
        self.ccht.set(lista[8])
        self.tww.set(lista[9])
        self.cm.set(lista[10])
        self.cbw.set(lista[11])
        self.wol.set(lista[12])
        self.wel.set(lista[13])
        self.rt.set(lista[14])
        self.em.set(lista[15])
        self.aiv.set(lista[16])
        self.acchv.set(lista[17])
        self.aev.set(lista[18])
        
    def createBlock(self,losses):
        
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
