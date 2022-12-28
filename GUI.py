#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 27 10:10:11 2022

@author: antonio
"""

import tkinter as tk
from tkinter import ttk
from tkinter import Menu
from tkinter import filedialog
from tkinter import messagebox
import csv
import sys

import GUI_Main
import GUI_Core
import GUI_Foil
import GUI_Tubes
import GUI_Disk
import bloque as bk

def main():
    root = tk.Tk()

    root.title("Calculo basico de calentamientos")

    # Cabecera de la entrada de datos

    frame1 = tk.Frame(root, width=800, height=100)
    frame1.grid(column=0, row=0)

    gui_main = GUI_Main.Gui_Main(frame1)

    # Cuerpo de la entrada de datos

    tabs = ttk.Notebook(root, width=800, height=500)
    tabs.grid(column=0, row=1)

    # Pestaña de entrada de datos del nucleo

    tab_nucleo= tk.Frame(tabs)
    tabs.add(tab_nucleo, text="Core")

    gui_core = GUI_Core.Gui_Core(tab_nucleo)

    # Pestaña de entrada de datos de la baja

    tab_foil= tk.Frame(tabs)
    tabs.add(tab_foil, text="Foil")

    gui_foil = GUI_Foil.Gui_Foil(tab_foil)

    # Pestaña de entrada de datos de los tubos

    tab_tubes= tk.Frame(tabs)
    tabs.add(tab_tubes, text="Tubes")

    gui_tubes = GUI_Tubes.Gui_Tubes(tab_tubes)

    # Pestaña de entrada de datos de la alta

    tab_disk= tk.Frame(tabs)
    tabs.add(tab_disk, text="Disk")

    gui_disk = GUI_Disk.Gui_Disk(tab_disk)

    # Menus de la ventana

    menu_bar = Menu(root)
    root.config(menu=menu_bar)

    menu1 = Menu(menu_bar)
    menu2 = Menu(menu_bar)
    
    # Menu 1 de la ventana

    menu_bar.add_cascade(label="File", menu=menu1)

    def new():
        erase = messagebox.askyesno(
            message='Are you sure you want to erase transformer data?',
            icon='question', title='Install')
        if erase:
            gui_main.newData()
            gui_core.newData()
            gui_foil.newData()
            gui_tubes.newData()
            gui_disk.newData()
    
    menu1.add_command(label="New", command = new)
  
    def save():
        filename = filedialog.asksaveasfilename(defaultextension=".trf", filetypes=[("transformer", ".trf")])
        with open(filename, "w", newline='') as csv_file:
            csv_writer = csv.writer(csv_file, dialect="excel")
            csv_writer.writerow(gui_main.getData())
            csv_writer.writerow(gui_core.getData())
            csv_writer.writerow(gui_foil.getData())
            csv_writer.writerow(gui_tubes.getData())
            csv_writer.writerow(gui_disk.getData())

    menu1.add_command(label="Save", command = save)

    def load():
        filename = filedialog.askopenfilename(defaultextension=".trf", filetypes=[("transformer", ".trf")])
        with open(filename, newline='') as csv_file:
            csv_reader = csv.reader(csv_file, dialect="excel")
            gui_main.setData(next(csv_reader))
            gui_core.setData(next(csv_reader))
            gui_foil.setData(next(csv_reader))
            gui_tubes.setData(next(csv_reader))
            gui_disk.setData(next(csv_reader))

    menu1.add_command(label="Load", command = load)

    def out():
        root.quit()
        root.destroy()
        sys.exit()

    menu1.add_command(label="Exit", command = out)

    # Menu 2 de la ventana

    menu_bar.add_cascade(label="Execute", menu=menu2)

    def noLoadTest():
        for bl in bk.bloques:
            del bl
        bk.contadorBloques = 0
        bk.bloques=[]
        
        mainData = gui_main.getData()
        gui_core.createBlock(losses=True)
        gui_foil.createBlock(losses=False)
        gui_tubes.createBlock()
        gui_disk.createBlock(losses=False)
    
    menu2.add_command(label="Run No Load Test", command = noLoadTest)
    
    def onLoadTest():
        for bl in bk.bloques:
            del bl
        bk.contadorBloques = 0
        bk.bloques=[]

        mainData = gui_main.getData()
        gui_core.createBlock(losses=False)
        gui_foil.createBlock(losses=True)
        gui_tubes.createBlock()
        gui_disk.createBlock(losses=True)
    
    menu2.add_command(label="Run On Load Test", command = onLoadTest)
    
    def serviceTest():
        for bl in bk.bloques:
            del bl
        bk.contadorBloques = 0
        bk.bloques=[]

        mainData = gui_main.getData()
        gui_core.createBlock(losses=True)
        gui_foil.createBlock(losses=True)
        gui_tubes.createBlock()
        gui_disk.createBlock(losses=True)
    
    menu2.add_command(label="Run Service Test", command = serviceTest)

    def saveBlocks():
        bk.guardaBloques()
    
    menu2.add_command(label="Save Blocks", command = saveBlocks)

    # bucle principal

    root.mainloop()

if __name__ == "__main__":
    main()
