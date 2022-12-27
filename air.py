#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 11 13:04:10 2022

@author: antonio
"""

import math

#  funcion para calcular la densidad del aire a una T (ºC)
def ro(t):
    tc = t - 273
    return (1.2722 
            - 4.9175e-3 * tc 
            + 1.9709e-5 * tc ** 2 
            - 4.3820e-8 * tc ** 3)

#  funcion para calcular el coef de expansión termico del aire a una T (ºC)    
def beta(t):
    tc = t - 273
    return(3.6581e-3 
           - 1.4270e-5 * tc
           + 5.9234e-8 * tc ** 2 
           - 1.3609e-10 * tc ** 3)

#  funcion para calcular el calor especifico del aire a una T (ºC)
def cp(t):
    tc = t - 273
    return(1006.1 
           + 1.2651e-2 * tc 
           + 5.4294e-4 * tc ** 2 
           - 5.3543e-7 * tc ** 3)
           
#  funcion para calcular la conductividad termica del aire a una T (ºC)
def lamb(t):
    tc = t - 273
    return (2.4465e-2 
            + 7.6664e-5 * tc
            - 2.4834e-8 * tc ** 2)

#  funcion para calcular la viscosidad cinematica del aire a una T (ºC)
def v(t):
    tc = t - 273
    return (1.3373e-5 
            + 8.6408e-8 * tc 
            + 1.0711e-10 * tc ** 2)

#  funcion para calcular el numero de reynolds
def reynolds(vel, l, ta, tw):
    t = (ta + tw) / 2
    return ((vel * l) / v(t))

#  funcion para calcular el número de Prandtl a la media de dos T (K)
def prandtl(ta, tw):
    t = (ta + tw) / 2
    a = lamb(t) / (cp(t) * ro(t))
    return (v(t) / a)

#  funcion para calcular el número de Grashof a la media de dos T (K)
#  sobre una superficie s de altura h
def grashof(ta, tw, s, h):
    t = (ta + tw) / 2
    return (((9.8 * beta(t) * (tw - ta) * s ** 3) / 
            (v(t) ** 2)) * (s / h))

#  funcion para calcular el número de Nusselt en un canal cilindrico de altura h
#  calentado por una sola cara, con una Tw(K) de la pared y una Tamb(K)  
def ANnusseltChannel1side(ta, tw, r1, r2, h):
    s = math.sqrt(r1 * r2) * math.log(r2 / r1)
    c1 = 0.0833
    c2 = 0.61
    g = grashof(ta, tw, s, h)
    p = prandtl(ta, tw)
    if (g == 0.0) or (p == 0.0):
        return(0.035)
    else:
        return((1.0 / ((c1 * g * p) ** 1.5) +
                1.0 / ((c2 * (g * p) ** 0.25) ** 1.5)) ** (-2.0 / 3.0))
        
#  funcion para calcular el número de Nusselt en un canal cilindrico de altura h
#  calentado por dos caras, con una Tw(K) de las paredes y una Tamb(K)  
def ANnusseltChannel2side(ta, tw, r1, r2, h):
    s = 0.5 * math.sqrt(r1 * r2) * math.log(r2 / r1)
    c1 = 0.3333
    c2 = 0.69
    g = grashof(ta, tw, s, h)
    p = prandtl(ta, tw)
    if (g == 0.0) or (p == 0.0):
        return(0.035)
    else:
        return((1.0 / ((c1 * g * p) ** 1.5) +
                1.0 / ((c2 * (g * p) ** 0.25) ** 1.5)) ** (-2.0 / 3.0))

#  funcion para calcular el número de Nusselt en una pared exterior de altura h
#  con una Tw(K) y una Tamb(K)  
def ANnusseltWall(ta, tw, h):
    g = grashof(ta, tw, h, h)
    p = prandtl(ta, tw)
    return(0.55 * (g * p) ** 0.25)

#  funcion para calcular el número de Nusselt en un canal cilindrico con ventilacion forzada
#  de altura l, calentado por dos caras, con una Tw(K) de las paredes y una Tamb(K)  
def AFnusseltChannel(ta, tw, r1, r2, l, vel):
    a = r1 / r2
    dh = r2 - r1
    r = reynolds(vel, dh, ta, tw)
    p = prandtl(ta, tw)
    re = r * (((1.0 + pow(a, 2)) * math.log(a) + (1.0 - pow(a, 2))) / 
             (pow((1.0 - a), 2) * math.log(a)))
    Ean_8 = (1.8 * math.log10(re) - 1.5) ** -2.0
    Ean_8 = Ean_8 / 8.0
    k1 = 1.07 + (900.0 / r) - 0.63 / (1.0 + 10.0 * p)
    fan = (0.75 * pow(a, -0.17) + (0.9 - 0.15 * pow(a, 0.6))) / (1 + a)
    nu = (Ean_8 * r * p) / (k1 + 12.7 * pow(Ean_8, 0.5) * pow(p, 2.0 / 3.0) - 1.0)
    nu = nu * (1 + pow(dh / l, 2.0 / 3.0)) * fan
    return nu

#  funcion para calcular el número de Nusselt en una pared exterior con ventilacion forzada
#  de altura l, con una Tw(K) de las paredes y una Tamb(K)  
def AFnusseltWall(ta, tw, l, vel):
    r = reynolds(vel, l, ta, tw)
    p = prandtl(ta, tw)
    Ean_8 = 0.037 * pow(r, -0.2)
    k1 = 1
    nu = (Ean_8 * r * p) / (k1 + 12.7 * pow(Ean_8, 0.5) * pow(p, (2.0 / 3.0)) - 1.0)
    return nu
