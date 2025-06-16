# -*- coding: utf-8 -*-
"""
Created on Thu Feb 15 22:39:29 2024

@author: felipe_neira
"""
# =============================================================================
# 
# =============================================================================
import kvzawpeyvm.wvzalkawe.kellual as kl
from kvzawpeyvm.wvzalkawe.koyam import Koyam
from kvzawpeyvm.rulpawirintukuwe.Reglas import reglas12
# =============================================================================
# Test
# =============================================================================
hemvl = "Chillkatuafiñ ka entuafiñ"
# =============================================================================
# def
# =============================================================================
hemvla = [hemvl.strip().lower() for hemvl in hemvl.split()]

def lef_pepikaam_hemvl(hemvl):
    hemvl1 = reglas12.rulpawe(hemvl.lower())
    hemvl = Koyam(hemvl1)
    hemvl.zewmakoyamvn()    
    
    hemvl.kaxvrowvn()
    hemvl = kl.kintuxokin(hemvl, 0)[0] 
    hemvlkawe = hemvl.wirintuku_hemvl2()
    hemvlkawe = [h.split('-')[1:] for h in hemvlkawe]
    
    wzkawe = hemvl.wirintuku_wz()
    wzkawe = [h.split('-')[1:] for h in wzkawe]
    
    return (hemvl1,  hemvlkawe, wzkawe)

test = [lef_pepikaam_hemvl(hemvl) for hemvl in hemvla]
# =============================================================================
# # =============================================================================
# # pepilkatun
# # =============================================================================
# 
# hemvl = reglas12.rulpawe(hemvl.lower())
# hemvl = Koyam(hemvl)
# hemvl.zewmakoyamvn()
# 
# # =============================================================================
# # kaxvrowvn
# # =============================================================================
# 
# hemvl.kaxvrowvn()
# hemvl = kl.kintuxokin(hemvl, 0)[0] 
# hemvlkawe = hemvl.wirintuku_hemvl2()
# hemvlkawew = [h.split('-')[1:] for h in hemvlkawe]
# 
# # =============================================================================
# # regex
# # =============================================================================
# 
# regexkawe = hemvl.wirintuku_regex()
# 
# # =============================================================================
# # Glosas
# # =============================================================================
# 
# wzkawe = hemvl.wirintuku_wz()
# wzkawe = [h.split('-')[1:] for h in wzkawe]
# 
# # =============================================================================
# # entun
# # =============================================================================
# 
# xipaalu[str(hemvl)] = (hemvlkawe, wzkawe)
# =============================================================================
