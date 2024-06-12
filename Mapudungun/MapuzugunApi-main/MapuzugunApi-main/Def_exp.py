# -*- coding: utf-8 -*-
"""
Created on Fri Feb 16 21:12:50 2024

@author: User
"""

# =============================================================================
# Librerias
# =============================================================================

from kvzawpeyvm.wvzalkawe.kellual import pepikaam_hemvl, prueba
import kvzawpeyvm.wvzalkawe.kellual as kl
import kvzawpeyvm.rulpawirintukuwe.KimamWirintukun as kz
from kvzawpeyvm.wvzalkawe.koyam import Koyam

# =============================================================================
# 
# =============================================================================

test = "chillkatuafiñ"
test1 = pepikaam_hemvl(test)


hemvla=[hemvl.strip().lower() for hemvl in test.split()]
xipaalu = dict()
for hemvl in hemvla:
    wirintukun = kz.chuchiWirintukun(hemvl)
    mvlica = True
    Nm=0
    koyam=None
    wirina=()
    for wirin in wirintukun:
        kkoyam = Koyam(wirin[1].lower())
        kkoyam.zewmakoyamvn()
        if Nm<len(kkoyam.kom_row):
            Nm=len(kkoyam.kom_row)
            koyam = kkoyam
            wirina = wirin
            

    
    if mvlica and len(wirintukun)>0 and type(koyam)!= type(None) and Nm>0:
        xipaalu['vy'] = hemvl
        
        xipaalu['wirintukun'] = kl.wirintukunVy[wirina[0]][0]
        rr = len(koyam.kom_row)
        while True:
            koyam.kaxvrowvn()
            if rr == len(koyam.kom_row):
                 break
            else:
                rr = len(koyam.kom_row)
                

    
        koyam = kl.kintuxokin(koyam,0)[0]            
        hemvlkawe = koyam.wirintuku_hemvl2()
        hemvlkawe =  [kl.wirintukunVy[wirina[0]][1](h) for h in hemvlkawe]
        hemvlkawew = [h.split('-')[1:] for h in hemvlkawe]
        regexkawe = koyam.wirintuku_regex()
        wzkawe = koyam.wirintuku_wz()
        wzkawe = [h.split('-')[1:] for h in wzkawe]
        aux = []
        aux2 = []
        

        for item in regexkawe:
            if item != '^':
                aux2.append(item)
            else:
                aux.append(aux2)
                aux2 = []
                
                
                
    xipaalu[str(hemvl)] = (hemvlkawe, wzkawe)
    
    
    
wirin[1]
