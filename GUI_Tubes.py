#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 27 12:55:15 2022

@author: antonio
"""

import tkinter as tk

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
        pass