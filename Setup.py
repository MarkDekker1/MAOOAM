# --------------------------------------------------------------------------- #
# Libraries
# --------------------------------------------------------------------------- #

import numpy as np
import sympy as sm
from scipy import integrate
import matplotlib.pyplot as plt
from PyDSTool import *
from AOTensor import *
import numpy as np
from PyDSTool.Toolbox import phaseplane

# --------------------------------------------------------------------------- #
# Parameters
# --------------------------------------------------------------------------- #

lda_0=20
d_0=1e-8
Co_0=300
Cpo0=Co_0/(Go*f0) * RR/(f0**2*L**2)
Cpa0=Co_0/(Ga*f0) * RR/(f0**2*L**2)/2/4
dp0=d_0/f0
Lpo_0=lda_0/(Go*f0)
Lpa_0=lda_0/(Ga*f0)
sc=1.0

AllVars=[]
icdict={}
for i in range(1,37):
    AllVars.append('X'+str(i))
    icdict[AllVars[i-1]]=0.0
    
# --------------------------------------------------------------------------- #
# Equations
# --------------------------------------------------------------------------- #

def CreateEquations_spec(lda,d,Co):
    global EQNS
    global AOT
    
    AOT=AOTTENSOR(lda,d,Co)
    
    EQNS={}    
    pars={}
    for r in range(0,37):
        pars[r]={}
        for i in range(0,37):
            pars[r][i]={}
            for k in range(0,37):
                pars[r][np.int(i)][np.int(k)]=0
            
    for r in range(0,36):
        for i in range(0,len(AOT[r])):
            j=AOT[r][i][0]
            k=AOT[r][i][1]
            v=AOT[r][i][2]
            pars[r][np.int(j)][np.int(k)]=v
    DSargs = args(name='MAOOAM')
    for i in range(0,36):
        EQ='0'
        for j in range(0,37):
            for k in range(0,37):
                if pars[i][j][k]!=0:
                    if j!=0:
                        EQ=EQ+' +'+str(pars[i][j][k])+'*'+AllVars[j-1]+'*'+AllVars[k-1]
                    if np.int(j)==0 and k!=0:
                        EQ=EQ+' +'+str(pars[i][j][k])+'*'+AllVars[k-1]
                    if j==0 and k==0:
                        EQ=EQ+' +'+str(pars[i][j][k])
        EQNS[AllVars[i]]=EQ
        
def CreateEquations_general():
    global EQNS
    global AOT
    
    AOT=AOTTENSOR(lda_0,d_0,Co_0)
    
    EQNS={}
    pars={}
    for r in range(0,37):
        pars[r]={}
        for i in range(0,37):
            pars[r][i]={}
            for k in range(0,37):
                pars[r][np.int(i)][np.int(k)]=0
            
    for r in range(0,36):
        for i in range(0,len(AOT[r])):
            j=AOT[r][i][0]
            k=AOT[r][i][1]
            v=AOT[r][i][2]
            pars[r][np.int(j)][np.int(k)]=v
    for i in range(0,36):
        EQ='0'
        for j in range(0,37):
            for k in range(0,37):
                if pars[i][j][k]!=0:
                    NUM=0
                    if i>=20 and i<=27 and k>=1 and k<=28 and j==0:
                        if k<=20:
                            EQ=EQ+' +'+str(pars[i][j][k])+'*(d/(0.0001032))/(9.689922480620155e-05)' +'*'+AllVars[k-1]
                            NUM=1
                        if k>=21:
                            k0=k-21
                            i0=i-20
                            val0=-(TensorOc['N'][i0,k0]*betp)/(TensorOc['M'][i0,i0]+G)
                            val1=-(TensorOc['M'][i0,i0]*(rp+dp0))/(TensorOc['M'][i0,i0]+G)
                            
                            if i0==k0:
                                EQ=EQ+' +('+str(val0)+'+'+str(val1)+'*(9.689922480620155e-05+d/0.0001032)/(9.689922480620155e-05+9.689922480620155e-05)' +')*'+AllVars[k-1]
                                NUM=1
                            else:
                                EQ=EQ+' +('+str(val0)+')*'+AllVars[k-1]
                                NUM=1
                    if i>=29-1 and j==0 and k==0:
                            EQ=EQ+' +'+str(pars[i][j][k])+'*Co*0.003333333333333333'  
                            NUM=1
                    if i>=11-1 and i<=20-1 and j==0 and k==0:
                            EQ=EQ+' +'+str(pars[i][j][k])+'*Co*0.0033333333333333335'
                            NUM=1   
                    if i>=28 and j==0 and k>=11 and k<=20:
                            EQ=EQ+' +'+str(pars[i][j][k])+'*'+AllVars[k-1]+'*(2.*1.*lda/(200000000.*0.0001032)+0.00032469320930232556)/(2.*1.0*0.000968992248062015+0.00032469320930232556)'
                            NUM=1
                    if i>=28 and j==0 and k>=29:
                            EQ=EQ+' +'+str(pars[i][j][k])+'*'+AllVars[k-1]+'*(lda/(200000000.*0.0001032)+0.0002512308139534884)/(0.0009689922480620155+0.0002512308139534884)'
                            NUM=1
                    if i>=10 and i<=19 and j==0 and k>=11 and k<=20:
                            i0=i-10
                            j0=k-11
                            if i0==j0:
                                val0=(-2.+2.*TensorAtm['a'][i0,i0]*sig0)
                                val1=-2.*(LSBpa+sc*Lpa_0)/val0
                                EQ=EQ+' +('+str(pars[i][j][k])+'+'+str(val1)+'+'+'2*(0.006493864186046512+1.0*lda/(10000000.*0.0001032))/'+str(val0)+')*'+AllVars[k-1]
                            else:
                                EQ=EQ+' +'+str(pars[i][j][k])+'*'+AllVars[k-1]
                            NUM=1
                    if i>=10 and i<=19 and j==0 and k>=29:
                            EQ=EQ+' +('+str(pars[i][j][k])
                            i0=i-10
                            j0=k-29
                            EQ=EQ+'-('+str(TensorAtm['s'][i0,j0])+'*0.01937984496124031)/(2-2*'+str(TensorAtm['a'][i0,i0])+'*0.1)'+'+('+str(TensorAtm['s'][i0,j0])+'*lda/(10000000.0*0.0001032))/(2-2*'+str(TensorAtm['a'][i0,i0])+'*0.1))'+'*'+AllVars[k-1]
                            NUM=1
                    if NUM==0:
                        if j!=0:
                            EQ=EQ+' +'+str(pars[i][j][k])+'*'+AllVars[j-1]+'*'+AllVars[k-1]
                        if np.int(j)==0 and k!=0:
                            EQ=EQ+' +'+str(pars[i][j][k])+'*'+AllVars[k-1]
                        if j==0 and k==0:
                            EQ=EQ+' +'+str(pars[i][j][k])
        EQNS[AllVars[i]]=EQ
    return EQNS
    
def Equations(state,t=0):
    global EQNS
    X1,X2,X3,X4,X5,X6,X7,X8,X9,X10,X11,X12,X13,X14,X15,X16,X17,X18,X19,X20,X21,X22,X23,X24,X25,X26,X27,X28,X29,X30,X31,X32,X33,X34,X35,X36 = state
    list2=[]
    for i in range(0,36):
        list2.append(eval(EQNS[AllVars[i]]))
    return list2

import re

def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False
        
def amountX(eqnterm):
    amount=0
    locs=[]
    for i in range(0,len(eqnterm)):
        if eqnterm[i]=='X':
            amount=amount+1
            locs.append(i)
    return amount,locs

def switch(i):
    if i==0:
        return 1
    if i==1:
        return 0

def CreateJacobian():
    global EQNS
    global JAC
    Jacob=[]
    for k in range(0,36):
        comps=EQNS[AllVars[k]].split()[1:]
        Jacobrow=list(np.zeros(36).astype(str))
        for j in range(0,len(comps)):
            varsy=[]
            for i in range(0,len(comps[j])):
                if comps[j][i]=='X':
                    var=comps[j][i]+comps[j][i+1]
                    if len(comps[j])>i+2:
                        if is_number(comps[j][i+2]):
                            var=var+comps[j][i+2]
                    varsy.append(var)
            for i in range(0,len(varsy)):
                num=re.findall(r"[-+]?\d*\.\d+|\d+",comps[j])
                
                varint=np.int(varsy[i][1:])
                
                if len(varsy)==2:
                    Jacobrow[varint-1]=num[0]+'*'+varsy[switch(i)]
                else:  
                    Jacobrow[varint-1]=num[0]
        Jacob.append(Jacobrow)
    Jacob2='['
    for i in range(0,36):
        Jacobrow2='['+Jacob[i][0]
        for k in range(1,36):
            Jacobrow2=Jacobrow2+','+Jacob[i][k]
        if i<35:
            Jacobrow2=Jacobrow2+'], '
        else:
            Jacobrow2=Jacobrow2+']'
            
        Jacob2=Jacob2+Jacobrow2
    JAC=Jacob2+']'
