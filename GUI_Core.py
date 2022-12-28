#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 27 12:55:15 2022

@author: antonio
"""

import tkinter as tk
import bloque as bk

class Gui_Core:
    
    def __init__(self, win):

        label1 = tk.Label(win, text="Core gross section:")
        self.gs = tk.StringVar()
        gs_entry = tk.Entry(win, textvariable=self.gs)
        label21 = tk.Label(win, text="cm2")

        label2 = tk.Label(win, text="Core diameter:")
        self.d = tk.StringVar()
        d_entry = tk.Entry(win, textvariable=self.d)
        label22 = tk.Label(win, text="mm")

        label3 = tk.Label(win, text="Core total weight:")
        self.w = tk.StringVar()
        w_entry = tk.Entry(win, textvariable=self.w)
        label23 = tk.Label(win, text="kg")

        label4 = tk.Label(win, text="Core center-center distance:")
        self.cc = tk.StringVar()
        cc_entry = tk.Entry(win, textvariable=self.cc)
        label24 = tk.Label(win, text="mm")

        label5 = tk.Label(win, text="Core window height:")
        self.wh = tk.StringVar()
        wh_entry = tk.Entry(win, textvariable=self.wh)
        label25 = tk.Label(win, text="mm")

        label6 = tk.Label(win, text="Max steel width:")
        self.mw = tk.StringVar()
        mw_entry = tk.Entry(win, textvariable=self.mw)
        label26 = tk.Label(win, text="mm")

        label7 = tk.Label(win, text="Core stacking height")
        self.sh = tk.StringVar()
        sh_entry = tk.Entry(win, textvariable=self.sh)
        label27 = tk.Label(win, text="mm")

        label8 = tk.Label(win, text="Core cooling channel number:")
        self.cchn = tk.StringVar()
        cchn_entry = tk.Entry(win, textvariable=self.cchn)
        label28 = tk.Label(win, text="ud")

        label9 = tk.Label(win, text="Core cooling channel thickness:")
        self.ccht = tk.StringVar()
        ccht_entry = tk.Entry(win, textvariable=self.ccht)
        label29 = tk.Label(win, text="mm")

        label10 = tk.Label(win, text="Core no load losses:")
        self.nl = tk.StringVar()
        nl_entry = tk.Entry(win, textvariable=self.nl)
        label30 = tk.Label(win, text="W")

        label11 = tk.Label(win, text="Core emissivity:")
        self.em = tk.StringVar()
        em_entry = tk.Entry(win, textvariable=self.em)
        label31 = tk.Label(win, text="p.u.")

        label12 = tk.Label(win, text="Cooling channels air velocity:")
        self.achv = tk.StringVar()
        achv_entry = tk.Entry(win, textvariable=self.achv)
        label32 = tk.Label(win, text="m/s")

        label13 = tk.Label(win, text="Outer side air velocity:")
        self.aev = tk.StringVar()
        aev_entry = tk.Entry(win, textvariable=self.aev)
        label33 = tk.Label(win, text="m/s")


        label1.grid(column=0, row=0, sticky="E")
        gs_entry.grid(column=1, row=0, sticky="WE")
        label21.grid(column=2, row=0, sticky="W")

        label2.grid(column=0, row=1, sticky="E")
        d_entry.grid(column=1, row=1, sticky="WE")
        label22.grid(column=2, row=1, sticky="W")

        label3.grid(column=0, row=2, sticky="E")
        w_entry.grid(column=1, row=2, sticky="WE")
        label23.grid(column=2, row=2, sticky="W")

        label4.grid(column=0, row=3, sticky="E")
        cc_entry.grid(column=1, row=3, sticky="WE")
        label24.grid(column=2, row=3, sticky="W")

        label5.grid(column=0, row=4, sticky="E")
        wh_entry.grid(column=1, row=4, sticky="WE")
        label25.grid(column=2, row=4, sticky="W")

        label6.grid(column=0, row=5, sticky="E")
        mw_entry.grid(column=1, row=5, sticky="WE")
        label26.grid(column=2, row=5, sticky="W")

        label7.grid(column=0, row=6, sticky="E")
        sh_entry.grid(column=1, row=6, sticky="WE")
        label27.grid(column=2, row=6, sticky="W")

        label8.grid(column=0, row=7, sticky="E")
        cchn_entry.grid(column=1, row=7, sticky="WE")
        label28.grid(column=2, row=7, sticky="W")

        label9.grid(column=0, row=8, sticky="E")
        ccht_entry.grid(column=1, row=8, sticky="WE")
        label29.grid(column=2, row=8, sticky="W")

        label10.grid(column=0, row=9, sticky="E")
        nl_entry.grid(column=1, row=9, sticky="WE")
        label30.grid(column=2, row=9, sticky="W")

        label11.grid(column=0, row=10, sticky="E")
        em_entry.grid(column=1, row=10, sticky="WE")
        label31.grid(column=2, row=10, sticky="W")

        label12.grid(column=0, row=11, sticky="E")
        achv_entry.grid(column=1, row=11, sticky="WE")
        label32.grid(column=2, row=11, sticky="W")

        label13.grid(column=0, row=12, sticky="E")
        aev_entry.grid(column=1, row=12, sticky="WE")
        label33.grid(column=2, row=12, sticky="W")

    def newData(self):
        self.gs.set("")
        self.d.set("")
        self.w.set("")
        self.cc.set("")
        self.wh.set("")
        self.mw.set("")
        self.sh.set("")
        self.cchn.set("")
        self.ccht.set("")
        self.nl.set("")
        self.em.set("")
        self.achv.set("")
        self.aev.set("")
        
    def getData(self):
        lista = list()
        lista.append(self.gs.get())
        lista.append(self.d.get())
        lista.append(self.w.get())
        lista.append(self.cc.get())
        lista.append(self.wh.get())
        lista.append(self.mw.get())
        lista.append(self.sh.get())
        lista.append(self.cchn.get())
        lista.append(self.ccht.get())
        lista.append(self.nl.get())
        lista.append(self.em.get())
        lista.append(self.achv.get())
        lista.append(self.aev.get())
        return lista
    
    def setData(self, lista):
        self.gs.set(lista[0])
        self.d.set(lista[1])
        self.w.set(lista[2])
        self.cc.set(lista[3])
        self.wh.set(lista[4])
        self.mw.set(lista[5])
        self.sh.set(lista[6])
        self.cchn.set(lista[7])
        self.ccht.set(lista[8])
        self.nl.set(lista[9])
        self.em.set(lista[10])
        self.achv.set(lista[11])
        self.aev.set(lista[12])
        
    def createBlock(self,losses):
        bl = bk.Bloque()
        
        bl.nInd = bk.contadorBloques
        
        bl.tAmb = 273.0 + 20.0
        
        bl.diamInt = 0.0
        a = pow((float(self.gs.get()) * 100.0 / 3.141592), 0.5)
        bl.diamExt = 2 * a / 1000.0
        bl.alt = float(self.wh.get()) / 1000.0
        bl.areaInt = 2.0 * (float(self.cchn.get()) * 
                            bl.alt * float(self.mw.get())) / 1000.0
        bl.areaExt = 2.0 * (float(self.mw.get()) + 
                            float(self.sh.get())) * bl.alt / 1000.0
        bl.emisiv = float(self.em.get())
        a = float(self.wh.get()) / (3.0 * float(self.wh.get()) + 2 * (2 * float(self.cc.get()))
                                    + float(self.mw.get()))
        bl.pesoFe = a * float(self.w.get())
        bl.pesoAl = 0.0
        bl.pesoCu = 0.0
        bl.pesoAisl = 0.0
        if losses:
            bl.pkOhm = a * float(self.nl.get())
        bl.pkAdi = 0.0
        bl.tRef = 0.0
        bl.temp = 273.0 + 20.0
        bl.incTemp = 1000.0
        bl.pk = 0.0
        bl.pConv = 0.0
        bl.pRad = 0.0
        bl.velAirChn = float(self.achv.get())
        bl.velAirExt = float(self.aev.get())
        
        bk.bloques.append(bl)