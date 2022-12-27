#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 27 12:55:15 2022

@author: antonio
"""

import tkinter as tk

class Gui_Disk:
    
    def __init__(self, win):

        label1 = tk.Label(win, text="Mechanical inner diameter:")
        self.dim = tk.StringVar()
        dim_entry = tk.Entry(win, textvariable=self.dim)
        label21 = tk.Label(win, text="mm")

        label2 = tk.Label(win, text="Mechanical outer diameter:")
        self.dom = tk.StringVar()
        dom_entry = tk.Entry(win, textvariable=self.dom)
        label22 = tk.Label(win, text="mm")

        label3 = tk.Label(win, text="Mechanical winding height:")
        self.wh = tk.StringVar()
        wh_entry = tk.Entry(win, textvariable=self.wh)
        label23 = tk.Label(win, text="mm")

        label4 = tk.Label(win, text="Inner insulation thickness:")
        self.iit = tk.StringVar()
        iit_entry = tk.Entry(win, textvariable=self.iit)
        label24 = tk.Label(win, text="mm")

        label5 = tk.Label(win, text="Outer insulation thickness:")
        self.oit = tk.StringVar()
        oit_entry = tk.Entry(win, textvariable=self.oit)
        label25 = tk.Label(win, text="mm")

        label6 = tk.Label(win, text="Total weight of 3 coils:")
        self.tww = tk.StringVar()
        tww_entry = tk.Entry(win, textvariable=self.tww)
        label26 = tk.Label(win, text="kg")

        label7 = tk.Label(win, text="Conductor Material:")
        self.cm = tk.StringVar()
        cm_entry = tk.Entry(win, textvariable=self.cm)
        label27 = tk.Label(win, text="Al / Cu")

        label8 = tk.Label(win, text="Conductor+Busbars weight:")
        self.cbw = tk.StringVar()
        cbw_entry = tk.Entry(win, textvariable=self.cbw)
        label28 = tk.Label(win, text="kg")

        label9 = tk.Label(win, text="Winding ohmic losses:")
        self.wol = tk.StringVar()
        wol_entry = tk.Entry(win, textvariable=self.wol)
        label29 = tk.Label(win, text="W")

        label10 = tk.Label(win, text="Winding eddy losses:")
        self.wel = tk.StringVar()
        wel_entry = tk.Entry(win, textvariable=self.wel)
        label30 = tk.Label(win, text="W")

        label11 = tk.Label(win, text="Reference temperature")
        self.rt = tk.StringVar()
        rt_entry = tk.Entry(win, textvariable=self.rt)
        label31 = tk.Label(win, text="ºC")

        label12 = tk.Label(win, text="Winding emissivity:")
        self.em = tk.StringVar()
        em_entry = tk.Entry(win, textvariable=self.em)
        label32 = tk.Label(win, text="p.u.")
        
            
        label1.grid(column=0, row=0, sticky="E")
        dim_entry.grid(column=1, row=0, sticky="WE")
        label21.grid(column=2, row=0, sticky="W")
       
        label2.grid(column=0, row=1, sticky="E")
        dom_entry.grid(column=1, row=1, sticky="WE")
        label22.grid(column=2, row=1, sticky="W")

        label3.grid(column=0, row=2, sticky="E")
        wh_entry.grid(column=1, row=2, sticky="WE")
        label23.grid(column=2, row=2, sticky="W")

        label4.grid(column=0, row=3, sticky="E")
        iit_entry.grid(column=1, row=3, sticky="WE")
        label24.grid(column=2, row=3, sticky="W")

        label5.grid(column=0, row=4, sticky="E")
        oit_entry.grid(column=1, row=4, sticky="WE")
        label25.grid(column=2, row=4, sticky="W")

        label6.grid(column=0, row=5, sticky="E")
        tww_entry.grid(column=1, row=5, sticky="WE")
        label26.grid(column=2, row=5, sticky="W")

        label7.grid(column=0, row=6, sticky="E")
        cm_entry.grid(column=1, row=6, sticky="WE")
        label27.grid(column=2, row=6, sticky="W")

        label8.grid(column=0, row=7, sticky="E")
        cbw_entry.grid(column=1, row=7, sticky="WE")
        label28.grid(column=2, row=7, sticky="W")
        
        label9.grid(column=0, row=8, sticky="E")
        wol_entry.grid(column=1, row=8, sticky="WE")
        label29.grid(column=2, row=8, sticky="W")        
        
        label10.grid(column=0, row=9, sticky="E")
        wel_entry.grid(column=1, row=9, sticky="WE")
        label30.grid(column=2, row=9, sticky="W")
        
        label11.grid(column=0, row=10, sticky="E")
        rt_entry.grid(column=1, row=10, sticky="WE")
        label31.grid(column=2, row=10, sticky="W")
        
        label12.grid(column=0, row=11, sticky="E")
        em_entry.grid(column=1, row=11, sticky="WE")
        label32.grid(column=2, row=11, sticky="W")

    def newData(self):
        self.dim.set("")
        self.dom.set("")
        self.wh.set("")
        self.iit.set("")
        self.oit.set("")
        self.tww.set("")
        self.cm.set("")
        self.cbw.set("")
        self.wol.set("")
        self.wel.set("")
        self.rt.set("")
        self.em.set("")
        
    def getData(self):
        lista = list()
        lista.append(self.dim.get())
        lista.append(self.dom.get())
        lista.append(self.wh.get())
        lista.append(self.iit.get())
        lista.append(self.oit.get())
        lista.append(self.tww.get())
        lista.append(self.cm.get())
        lista.append(self.cbw.get())
        lista.append(self.wol.get())
        lista.append(self.wel.get())
        lista.append(self.rt.get())
        lista.append(self.em.get())
        return lista
    
    def setData(self, lista):
        self.dim.set(lista[0])
        self.dom.set(lista[1])
        self.wh.set(lista[2])
        self.iit.set(lista[3])
        self.oit.set(lista[4])
        self.tww.set(lista[5])
        self.cm.set(lista[6])
        self.cbw.set(lista[7])
        self.wol.set(lista[8])
        self.wel.set(lista[9])
        self.rt.set(lista[10])
        self.em.set(lista[11])
        
    def createBlock(self,losses):
        pass