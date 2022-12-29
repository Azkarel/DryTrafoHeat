#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 29 12:42:25 2022

@author: antonio
"""

import tkinter as tk

import bloque as bk

def calculaCalentamiento(regimen):
    
    flag = True
    iteracion = 1
    
    while (flag and (iteracion<1440)):
    
        flag = False
    
        for bl in bk.bloques:
        
            print(iteracion, end=", ")
            print(bl.nInd, end=", ")
            print(round((bl.temp - bl.tAmb), 2), end=", ")
            print(round(bl.pk, 2), end=", ")
            print(round(bl.pConv, 2), end=", ")
            print(round(bl.pRad, 2))
        
            bl.actualizaTemp(regimen, 60.0)
        
            bl.temp = bl.temp + bl.incTemp
            if bl.incTemp > 0.005:
                flag = True
    
        print("\n")

        iteracion = iteracion + 1

