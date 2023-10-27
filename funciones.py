#!/usr/bin/env python
# coding: utf-8



def media(datos):
    x= []
    for j in datos:
        if j == j:
            x.append(j)
    sum_ = 0
    for i in x:
        sum_ = sum_ + i
    return sum_/len(x)




def varianza(datos):
    y= []
    for j in datos:
        if j == j:
            y.append(j)
    
    n = len(y)
    
    prom = sum(y) / n
    suma_sq = sum((x - prom) ** 2 for x in y)
    
    var = suma_sq / (n - 1)

    
    return var




import math

def desv_estandar(datos):
    y= []
    for j in datos:
        if j == j:
            y.append(j)
    n = len(y)
    
    prom = sum(y) / n
    suma_sq = sum((x - prom) ** 2 for x in y)
    
    var = suma_sq / (n - 1)
    
    desv_estandar = math.sqrt(var)
    
    return desv_estandar




def mediana(datos):
    x= []
    for j in datos:
        if j == j:
            x.append(j)
    datos_2 = sorted(x)
    n = len(datos_2)

    if n % 2 == 0:
        medio = datos_2[n // 2 - 1]
        medio1 = datos_2[n // 2]
        mediana = (medio + medio1) / 2
    else:
        
        mediana = datos_2[n // 2]

    return mediana


def moda(datos):    
    x= []
    for j in datos:
        if j == j:
            x.append(j)

    frecuencia = {}
    for valor in x:
        frecuencia[valor] = frecuencia.get(valor, 0) + 1

    moda = None
    frecuencia_maxima = 0
    for valor, count in frecuencia.items():
        if count > frecuencia_maxima:
            moda = valor
            frecuencia_maxima = count

    return moda


def cuartiles(datos,cuar):   
    x= []
    for j in datos:
        if j == j:
            x.append(j)

    x = sorted(x)
    N_cuar = (cuar/4)*(len(x)-1)
    p = N_cuar - int(N_cuar)
    
    if p == 0:
        return x[int(N_cuar)]
    else:
        return x[int(N_cuar)]*(1-p)+ x[int(N_cuar)+1]*p


def rango_interc(datos):
    x= []
    for j in datos:
        if j == j:
            x.append(j)
    datos_2 = sorted(x)
    n = len(datos_2)

    q1_index = (n + 1) // 4
    q3_index = 3 * q1_index
    q1 = datos_2[q1_index - 1]
    q3 = datos_2[q3_index - 1]

    iqran = q3 - q1
    return iqran
    
def rango(datos):
    x= []
    for j in datos:
        if j == j:
            x.append(j)

    if len(x) == 0:
        
        return None

    rango = max(x) - min(x)
    return rango


def percentiles(x,per):
    y=[]
    for i in x:
        if i == i:
            y.append(i)
    y= sorted(y)
    vper = (per/100)*(len(y)-1)
    p = vper - int(vper)
    
    if p == 0:
        perce = y[int(vper)]
    else:
        perce = y[int(vper)]*(1-p) + y[int(vper)+1]*p
        
    return perce

def mad(datos):
    y= []
    for j in datos:
        if j == j:
            y.append(j)
    datos_2 = sorted(y)
    n = len(datos_2)

    if n % 2 == 0:
        medio = datos_2[n // 2 - 1]
        medio1 = datos_2[n // 2]
        mediana = (medio + medio1) / 2
    else:
        mediana = datos_2[n // 2]

    
    desv_abs = [abs(x - mediana) for x in datos]
    
    datos_3 = sorted(desv_abs)
    n2 = len(datos_3)

    if n2 % 2 == 0:
        medio02 = datos_3[n2 // 2 - 1]
        medio12 = datos_3[n2 // 2]
        mad = (medio02 + medio12) / 2
    else:
        mad = datos_3[n // 2]


    return mad

        
        
        
        
   