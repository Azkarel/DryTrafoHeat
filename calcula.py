#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 29 12:42:25 2022

@author: antonio
"""

import tkinter as tk
import matplotlib.pyplot as plt

import bloque as bk

def calculaCalentamiento(regimen):
    
    flag = True
    iteracion = 1
    x = list()
    y1 = list()
    y2 = list()
    y3 = list()
    y4 = list()
    
    while (flag and (iteracion<1440)):
    
        flag = False
        ysub1 = list()
        ysub2 = list()
        ysub3 = list()
        ysub4 = list()
   
        for bl in bk.bloques:
 
            print(iteracion, end=", ")
            
            print(bl.nInd, end=", ")
            
            temperatureIncrement = bl.temp - bl.tAmb
            print(round(temperatureIncrement, 2), end=", ")
            ysub1.append(temperatureIncrement) 
            
            print(round(bl.pk, 2), end=", ")
            ysub2.append(bl.pk) 
            
            print(round(bl.pConv, 2), end=", ")
            ysub3.append(bl.pConv) 
            
            print(round(bl.pRad, 2))
            ysub4.append(bl.pRad) 
        
            bl.actualizaTemp(regimen, 60.0)
        
            bl.temp = bl.temp + bl.incTemp
            if bl.incTemp > 0.005:
                flag = True
    
        print("\n")
        
        x.append(iteracion)
        y1.append(ysub1)
        y2.append(ysub2)
        y3.append(ysub3)
        y4.append(ysub4)

        iteracion = iteracion + 1

    fig, ax = plt.subplots()
    ax.plot(x, y1)
    ax.set_title('Incrementos de Temperatura')
    plt.show()
    
    fig, ax = plt.subplots()
    ax.plot(x, y2)
    ax.set_title('Perdidas generadas')
    plt.show()
    
    fig, ax = plt.subplots()
    ax.plot(x, y3)
    ax.set_title('Perdidas disitadas por conveccion')
    plt.show()
    
    fig, ax = plt.subplots()
    ax.plot(x, y4)
    ax.set_title('Perdidas disitadas por radiacion')
    plt.show()
