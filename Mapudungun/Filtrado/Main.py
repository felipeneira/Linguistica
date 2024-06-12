# -*- coding: utf-8 -*-
"""
Created on Sat Mar 16 18:38:12 2024

@author: User
"""
# =============================================================================
# Texto
# =============================================================================

import lifkvnvpeyvm as lif

texto = lif.entukvnvn_hemvl()

# =============================================================================
# Katrvhemvl
# =============================================================================

from we_pepikaam_hemvl import lef_pepikaam_hemvl

# =============================================================================
# 
# =============================================================================

hemvl = "Chillkatuafiñ ka entuafiñ"
hemvla = [hemvl.strip().lower() for hemvl in hemvl.split()]
test = [lef_pepikaam_hemvl(hemvl) for hemvl in hemvla]


