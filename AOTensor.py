# --------------------------------------------------------------------------- #
# EQUATION TENSOR FOR COUPLED MODEL
# --------------------------------------------------------------------------- #

# --------------------------------------------------------------------------- #
# PREAMBLE AND VARIABLE DECLARATION
# --------------------------------------------------------------------------- #
from Parameters import *
from InnerProductComputation import *
import Tensor
import numpy as np

# --------------------------------------------------------------------------- #
# PREAMBLE AND FUNCTION DECLARATIONS
# --------------------------------------------------------------------------- #
def psi(i):
    return i+1

def theta(i):
    return i+natm+1

def A(i):
    return i+2*natm+1

def T(i):
    return i+2*natm+noc+1

def kdelta(i,j):
    kdelta=0
    if i==j:
        kdelta=1
    return kdelta
    
def nelems(i):
    count=0
    for j in range(0,ndim):
        if AOT[i,j,2]==0:#and AOT[i,j,0]==0 and AOT[i,j,1]==0:
            a=2
        else:
            count=count+1
    return count

# --------------------------------------------------------------------------- #
# SUBROUTINES
# --------------------------------------------------------------------------- #
def coeff(i,j,k,v):
    global AOT
    #if np.abs(v)>=real_eps:
    nl=nelems(i)+1
    if j<=k:
        AOT[i,nl,0]=j
        AOT[i,nl,1]=k
    else:
        AOT[i,nl,0]=k
        AOT[i,nl,1]=j
    AOT[i,nl,2]=v

def simplify_aotensor():
    global AOT
    for i in range(0,ndim):
        nl=nelems(i)
        for li in range(1,nl)[::-1]:
            j=AOT[i,li,0]
            k=AOT[i,li,1]
            for lii in range(0,li-1)[::-1]:
                if j==AOT[i,lii,0] and k==AOT[i,lii,1]:
                    AOT[i,lii,2]=AOT[i,lii,2]+AOT[i,li,2]
                    for liii in range(li+1,nl):
                        AOT[i,liii-1,0]=AOT[i,liii,0]
                        AOT[i,liii-1,1]=AOT[i,liii,1]
                        AOT[i,liii-1,2]=AOT[i,liii,2]
        nl=nelems(i)
        for li in range(0,nl):
            while np.abs(AOT[i,li,2])<real_eps:
                for liii in range(li+1,nl):
                    AOT[i,liii-1,0]=AOT[i,liii,0]
                    AOT[i,liii-1,1]=AOT[i,liii,1]
                    AOT[i,liii-1,2]=AOT[i,liii,2]
                    
def simplify_aotensor2():
    global AOT
    for i in range(0,ndim):
        nl=nelems(i)+1
        for ni in range(0,nl):
            j=AOT[i,ni,0]
            k=AOT[i,ni,1]
            for nii in range(ni+1,nl):
                if AOT[i,nii,0]==j and AOT[i,nii,1]==k:
                    AOT[i,ni,2]=AOT[i,nii,2]+AOT[i,ni,2]
                    AOT[i,nii,0]=0
                    AOT[i,nii,1]=0
                    AOT[i,nii,2]=0
    for i in range(0,ndim):
        for k in range(0,ndim):
            for ni in range(0,ndim-1):
                if AOT[i,ni,2]==0:
                    AOT[i,ni,0]=AOT[i,ni+1,0]
                    AOT[i,ni,1]=AOT[i,ni+1,1]
                    AOT[i,ni,2]=AOT[i,ni+1,2]
                    
                    AOT[i,ni+1,0]=0
                    AOT[i,ni+1,1]=0
                    AOT[i,ni+1,2]=0       
                    
def nullify_tensor():
    global AOT
    AOT2=[]
    for i in range(0,ndim):
        vec=[]
        for j in range(0,ndim):
            if AOT[i,j,2]!=0:
                vec.append(j)
        AOT2.append(AOT[i,vec])
    AOT=AOT2
                    
def add_count(i,j,k,v):
    global count_elems
    if np.abs(v)>=real_eps:
        count_elems[i]=count_elems[i]+1-1
        
def compute_aotensor(func):
    func(theta(0),0,0,(Cpa/(1.-TensorAtm['a'][0,0]*sig0)))
    for i in range(0,natm):
        for j in range(0,natm):
            func(psi(i),psi(j),0,-(((TensorAtm['c'][i,j]*betp)/TensorAtm['a'][i,i]))-(kd*kdelta(i,j))/2.)
            func(theta(i),psi(j),0,(TensorAtm['a'][i,j]*kd*sig0)/(-2.+2.*TensorAtm['a'][i,i]*sig0))
            func(psi(i),theta(j),0,(kd*kdelta(i,j))/2.)
            func(theta(i),theta(j),0,(-((sig0*(2.*TensorAtm['c'][i,j]*betp+
            TensorAtm['a'][i,j]*(kd+4.*kdp))))+2.*(LSBpa+sc*Lpa)*kdelta(i,j))/
            (-2.+2.*TensorAtm['a'][i,i]*sig0))        
            for k in range(0,natm):
                func(psi(i),psi(j),psi(k),-((TensorAtm['b'][i,j,k]/TensorAtm['a'][i,i])))
                func(psi(i),theta(j),theta(k),-((TensorAtm['b'][i,j,k]/TensorAtm['a'][i,i])))
                func(theta(i),psi(j),theta(k),(TensorAtm['g'][i,j,k]-TensorAtm['b'][i,j,k]*sig0)/
                (-1.+TensorAtm['a'][i,i]*sig0))
                func(theta(i),theta(j),psi(k),(TensorAtm['b'][i,j,k]*sig0)/(1.-TensorAtm['a'][i,i]*sig0))
        for j in range(0,noc):
            func(psi(i),A(j),0,kd*TensorAtm['d'][i,j]/(2.*TensorAtm['a'][i,i]))
            func(theta(i),A(j),0,kd*(TensorAtm['d'][i,j]*sig0)/(2.-2.*TensorAtm['a'][i,i]*sig0))
            func(theta(i),T(j),0,TensorAtm['s'][i,j]*(2.*LSBpo+Lpa)/(2.-2.*TensorAtm['a'][i,i]*sig0))
    for i in range(0,noc):
        for j in range(0,natm):
            func(A(i),psi(j),0,TensorOc['K'][i,j]*dp/(TensorOc['M'][i,i]+G))
            func(A(i),theta(j),0,-(TensorOc['K'][i,j])*dp/(TensorOc['M'][i,i]+G))
        for j in range(0,noc):
            func(A(i),A(j),0,-((TensorOc['N'][i,j]*betp+TensorOc['M'][i,i]*(rp+dp)
            *kdelta(i,j)))/(TensorOc['M'][i,i]+G))
            for k in range(0,noc):
                func(A(i),A(j),A(k),-(TensorOc['C'][i,j,k])/(TensorOc['M'][i,i]+G))
    for i in range(0,noc):
        func(T(i),0,0,Cpo*TensorOc['W'][i,0])
        for j in range(0,natm):
            func(T(i),theta(j),0,TensorOc['W'][i,j]*(2.*sc*Lpo+sBpa))
        for j in range(0,noc):
            func(T(i),T(j),0,-(Lpo+sBpo)*kdelta(i,j))
            for k in range(0,noc):
                func(T(i),A(j),T(k),-(TensorOc['O'][i,j,k]))

def AOTTENSOR(lda,d,Co):
    global Cpa
    global Cpo
    global Lpo
    global Lpa
    global dp
    global real_eps
    global count_elems
    global AOT
        
    Cpo=Co/(Go*f0) * RR/(f0**2.*L**2.)
    Ca=Co/4.
    Cpa=Ca/(Ga*f0) * RR/(f0**2.*L**2.)/2.
    Lpo=lda/(Go*f0)
    Lpa=lda/(Ga*f0)
    dp=d/f0
    
    n0=0
    real_eps = 2.2204460492503131e-16
    count_elems=np.zeros(ndim+1)
    dimensions={'i':36,'j':0,'k':0,'v':0,'n':0}
    AOT=np.zeros(shape=(ndim+1,ndim+1,3))
    
    # --------------------------------------------------------------------------- #
    # INITIALIZATION ROUTINE
    # --------------------------------------------------------------------------- #
    
    compute_aotensor(add_count)
    
    compute_aotensor(coeff)
    simplify_aotensor2()
    AOT=AOT[1:]
    nullify_tensor()
    return AOT