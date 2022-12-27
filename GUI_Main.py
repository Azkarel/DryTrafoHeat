#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 27 12:55:15 2022

@author: antonio
"""

import tkinter as tk

class Gui_Main:
    
    def __init__(self, win):

        label1 = tk.Label(win, text="Design:")
        self.design = tk.StringVar()        
        design_entry = tk.Entry(win, textvariable=self.design)

        label2 = tk.Label(win, text="Type of Vent:")
        self.vent = tk.StringVar()
        vent_entry = tk.Entry(win, textvariable=self.vent)

        label3 = tk.Label(win, text="Winding Shells Number:")
        self.n_shells = tk.StringVar()
        n_shells_entry = tk.Entry(win, textvariable=self.n_shells)

        label4 = tk.Label(win, text="Winding Axial Number:")
        self.n_axials = tk.StringVar()
        n_axials_entry = tk.Entry(win, textvariable=self.n_axials)
        
        
        label1.grid(column=0, row=0, sticky="E")
        design_entry.grid(column=1, row=0, sticky="WE")
        
        label2.grid(column=0, row=1, sticky="E")
        vent_entry.grid(column=1, row=1, sticky="WE")
        
        label3.grid(column=2, row=0, sticky="E")
        n_shells_entry.grid(column=3, row=0, sticky="WE")
        
        label4.grid(column=2, row=1, sticky="E")
        n_axials_entry.grid(column=3, row=1, sticky="WE")


    def newData(self):
        self.design.set("")
        self.vent.set("")
        self.n_shells.set("")
        self.n_axials.set("")

    def getData(self):
        lista = list()
        lista.append(self.design.get())
        lista.append(self.vent.get())
        lista.append(self.n_shells.get())
        lista.append(self.n_axials.get())
        return lista
    
    def setData(self, lista):
        self.design.set(lista[0])
        self.vent.set(lista[1])
        self.n_shells.set(lista[2])
        self.n_axials.set(lista[3])
        
        