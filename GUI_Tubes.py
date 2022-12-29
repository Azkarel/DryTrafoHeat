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

        label1 = tk.Label(win, text="Tubes height:")
        self.th = tk.StringVar()
        th_entry = tk.Entry(win, textvariable=self.th)
        label21 = tk.Label(win, text="mm")

        label2 = tk.Label(win, text="Diam Int tubes space:")
        self.dic = tk.StringVar()
        dic_entry = tk.Entry(win, textvariable=self.dic)
        label22 = tk.Label(win, text="mm")

        label3 = tk.Label(win, text="Diam Ext tubes space:")
        self.doc = tk.StringVar()
        doc_entry = tk.Entry(win, textvariable=self.doc)
        label23 = tk.Label(win, text="mm")

        label4 = tk.Label(win, text="Number of tubes:")
        self.tn = tk.StringVar()
        tn_entry = tk.Entry(win, textvariable=self.tn)
        label24 = tk.Label(win, text="ud")

        label5 = tk.Label(win, text="Tubes thickness:")
        self.tt = tk.StringVar()
        tt_entry = tk.Entry(win, textvariable=self.tt)
        label25 = tk.Label(win, text="mm")

        label6 = tk.Label(win, text="Distance between tubes:")
        self.dbt = tk.StringVar()
        dbt_entry = tk.Entry(win, textvariable=self.dbt)
        label26 = tk.Label(win, text="mm")

        label7 = tk.Label(win, text="Tubes density:")
        self.td = tk.StringVar()
        td_entry = tk.Entry(win, textvariable=self.td)
        label27 = tk.Label(win, text="mm")
        
        label8 = tk.Label(win, text="Tubes emmisivity:")
        self.em = tk.StringVar()
        em_entry = tk.Entry(win, textvariable=self.em)
        label28 = tk.Label(win, text="p.u.")

        label9 = tk.Label(win, text="Inner air velocity:")
        self.aiv = tk.StringVar()
        aiv_entry = tk.Entry(win, textvariable=self.aiv)
        label29 = tk.Label(win, text="m/s")

        label10 = tk.Label(win, text="Inter tubes air velocity:")
        self.atv = tk.StringVar()
        atv_entry = tk.Entry(win, textvariable=self.atv)
        label30 = tk.Label(win, text="m/s")

        label11 = tk.Label(win, text="Outer side air velocity:")
        self.aev = tk.StringVar()
        aev_entry = tk.Entry(win, textvariable=self.aev)
        label31 = tk.Label(win, text="m/s")


        label1.grid(column=0, row=0, sticky="E")
        th_entry.grid(column=1, row=0, sticky="WE")
        label21.grid(column=2, row=0, sticky="W")

        label2.grid(column=0, row=1, sticky="E")
        dic_entry.grid(column=1, row=1, sticky="WE")
        label22.grid(column=2, row=1, sticky="W")

        label3.grid(column=0, row=2, sticky="E")
        doc_entry.grid(column=1, row=2, sticky="WE")
        label23.grid(column=2, row=2, sticky="W")

        label4.grid(column=0, row=3, sticky="E")
        tn_entry.grid(column=1, row=3, sticky="WE")
        label24.grid(column=2, row=3, sticky="W")

        label5.grid(column=0, row=4, sticky="E")
        tt_entry.grid(column=1, row=4, sticky="WE")
        label25.grid(column=2, row=4, sticky="W")

        label6.grid(column=0, row=5, sticky="E")
        dbt_entry.grid(column=1, row=5, sticky="WE")
        label26.grid(column=2, row=5, sticky="W")

        label7.grid(column=0, row=6, sticky="E")
        td_entry.grid(column=1, row=6, sticky="WE")
        label27.grid(column=2, row=6, sticky="W")

        label8.grid(column=0, row=7, sticky="E")
        em_entry.grid(column=1, row=7, sticky="WE")
        label28.grid(column=2, row=7, sticky="W")

        label9.grid(column=0, row=8, sticky="E")
        aiv_entry.grid(column=1, row=8, sticky="WE")
        label29.grid(column=2, row=8, sticky="W")

        label10.grid(column=0, row=9, sticky="E")
        atv_entry.grid(column=1, row=9, sticky="WE")
        label30.grid(column=2, row=9, sticky="W")

        label11.grid(column=0, row=10, sticky="E")
        aev_entry.grid(column=1, row=10, sticky="WE")
        label31.grid(column=2, row=10, sticky="W")


    def newData(self):
        self.th.set("")
        self.dic.set("")
        self.doc.set("")
        self.tn.set("")
        self.tt.set("")
        self.dbt.set("")
        self.td.set("")
        self.em.set("")
        self.aiv.set("")
        self.atv.set("")
        self.aev.set("")

    def getData(self):
        lista = list()
        lista.append(self.th.get())
        lista.append(self.dic.get())
        lista.append(self.doc.get())
        lista.append(self.tn.get())
        lista.append(self.tt.get())
        lista.append(self.dbt.get())
        lista.append(self.td.get())
        lista.append(self.em.get())
        lista.append(self.aiv.get())
        lista.append(self.atv.get())
        lista.append(self.aev.get())
        return lista
    
    def setData(self, lista):
        self.th.set(lista[0])
        self.dic.set(lista[1])
        self.doc.set(lista[2])       
        self.tn.set(lista[3])
        self.tt.set(lista[4])
        self.dbt.set(lista[5])
        self.td.set(lista[6])
        self.em.set(lista[7])
        self.aiv.set(lista[8])
        self.atv.set(lista[9])
        self.aev.set(lista[10])     
           
    def createBlock(self):
        
        radialTubos = (int(self.tn.get()) * float(self.tt.get()) + 
                      (int(self.tn.get()) - 1) * float(self.dbt.get()))
        radialTubos = radialTubos / 1000.0

        diamMedTotal = (float(self.dic.get()) + float(self.doc.get())) / 2.0 / 1000.0
       
        for n in range(int(self.tn.get())):
            bl = bk.Bloque()
            
            bk.contadorBloques = bk.contadorBloques + 1
            bl.nInd = bk.contadorBloques
            
            bl.tAmb = 273.0 + 20.0
            
            bl.diamInt = (diamMedTotal - radialTubos +
                          2.0 * n * (float(self.tt.get()) + 
                                     float(self.dbt.get())) / 1000.0)
            
            bl.diamExt = bl.diamInt + 2 * (float(self.tt.get())) / 1000.0
            
            diamMed = (bl.diamInt + bl.diamExt) / 2.0
            
            bl.alt = float(self.th.get()) / 1000.0
            bl.areaInt = 3.141592 * bl.diamInt * bl.alt
            bl.areaExt = 3.141592 * bl.diamExt * bl.alt
            
            bl.emisiv = float(self.em.get())
            
            bl.pesoFe = 0.0
            bl.pesoCu = 0.0
            bl.pesoAl = 0.0
            bl.pesoAisl =(2.0 * 3.141592 * diamMed * bl.alt * 
                          float(self.tt.get())) * float(self.td.get())
            
            bl.pkOhm = 0.0
            bl.pkAdi = 0.0
            
            bl.tRef = 0.0
            bl.temp = 273.0 + 20.0
            bl.incTemp = 1000.0
            
            bl.pk = 0.0
            bl.pConv = 0.0
            bl.pRad = 0.0
            
            bl.velAirInt = float(self.atv.get())
            bl.velAirExt = float(self.atv.get())
            if n == 0:
                bl.velAirInt = float(self.aiv.get())
            if n == int(self.tn.get()) - 1:
                bl.velAirExt = float(self.aev.get())

            bk.bloques.append(bl)
