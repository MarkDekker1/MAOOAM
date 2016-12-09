# --------------------------------------------------------------------------- #
# Reduce model order
# --------------------------------------------------------------------------- #

from Setup import *

def Reductor(amount,EQNS,icdict,extrapars):
        
    ToKeep=[]    
    for i in [0,10,20,28]:
        for j in range(0,amount):
            ToKeep.append(i+j)
            
    extrapars={}
    
    for i in range(0,36):
        if i not in ToKeep:
            del EQNS[AllVars[i]]
            del icdict[AllVars[i]]
            extrapars[AllVars[i]]=0
    
    return EQNS,icdict,extrapars