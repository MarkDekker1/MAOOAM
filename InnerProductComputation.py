# --------------------------------------------------------------------------- #
# INNER PRODUCTS BETWEEN TRUNCATED SET OF BASIS FUNCTIONS FOR PSI FIELDS
# --------------------------------------------------------------------------- #
#  see: Cehelsky, P., & Tung, K. K. : Theories of multiple equilibria and
#  weather regimes-A critical reexamination. Part II: Baroclinic two-layer
#  models. Journal of the atmospheric sciences, 44(21), 3282-3303, 1987.

# --------------------------------------------------------------------------- #
# PREAMBLE AND VARIABLE DECLARATION
# --------------------------------------------------------------------------- #
from Parameters import *
import numpy as np

#ATMOSPHERIC TENSORS
TensorAtm={
'a':np.zeros(shape=(natm,natm)),
'c':np.zeros(shape=(natm,natm)),
'd':np.zeros(shape=(natm,natm)),
's':np.zeros(shape=(natm,natm)),
'b':np.zeros(shape=(natm,natm,natm)),
'g':np.zeros(shape=(natm,natm,natm))
}

#OCEANIC TENSORS
TensorOc={
'K':np.zeros(shape=(noc,natm)),
'M':np.zeros(shape=(noc,noc)),
'N':np.zeros(shape=(noc,noc)),
'W':np.zeros(shape=(noc,natm)),
'O':np.zeros(shape=(noc,noc,noc)),
'C':np.zeros(shape=(noc,noc,noc))
}
  
# --------------------------------------------------------------------------- #
# HELPER FUNCTIONS
# --------------------------------------------------------------------------- #
def B1(Pi,Pj,Pk):
    return (Pk+Pj)/(Pi)

def B2(Pi,Pj,Pk):
    return (Pk-Pj)/(Pi)
    
def delta(r):
    if r==0:
        return 1.
    else:
        return 0.

def flambda(r):
    if np.mod(r,2)==0:
        return 0.
    else:
        return 1.
        
def S1(Pj,Pk,Mj,Hk):
    return -((Pk*Mj+Pj*Hk))/2.

def S2(Pj,Pk,Mj,Hk):
    return (Pk*Mj-Pj*Hk)/2.

def S3(Pj,Pk,Hj,Hk):
    return (Pk*Hj+Pj*Hk)/2.

def S4(Pj,Pk,Hj,Hk):
    return (Pk*Hj-Pj*Hk)/2.
    
# --------------------------------------------------------------------------- #
# INITIALIZATION ROUTINE
# --------------------------------------------------------------------------- #
atypes=[None]*natm
awavenum=np.zeros(shape=(natm,2))
owavenum=np.zeros(shape=(noc,2))

atypes=['A','K','L','A','K','L','K','L','K','L']
awavenum=[[0.,1.],
          [1.,1.],
          [1.,1.],
          [0.,2.],
          [1.,2.],
          [1.,2.],
          [2.,1.],
          [2.,1.],
          [2.,2.],
          [2.,2.],
          ]
owavenum=[[1.,1.],
          [1.,2.],
          [1.,3.],
          [1.,4.],
          [2.,1.],
          [2.,2.],
          [2.,3.],
          [2.,4.],
          ]
    
# --------------------------------------------------------------------------- #
# ATMOSPHERE EQUATION INNER PRODUCTS
# --------------------------------------------------------------------------- #
# TENSOR a; a(i,j)=(F_i,\nabla^2 F_j)
for i in range(0,natm):
    Ti=awavenum[i]
    TensorAtm['a'][i,i]=-(n**2.) * Ti[0]**2.-Ti[1]**2.

# TENSOR g; g_{i,j,k} = (F_i, J(F_j, F_k))
for i in range(0,natm):
    for j in range(0,natm):
        for k in range(0,natm):
            Ti = awavenum[i]
            Tj = awavenum[j]
            Tk = awavenum[k]
            val=0.
            if atypes[i]=='A' and atypes[j]=='K' and atypes[k]=='L':
                vb1 = B1(Ti[1],Tj[1],Tk[1])
                vb2 = B2(Ti[1],Tj[1],Tk[1])
                val = -2*np.sqrt(2.)/np.pi*Tj[0]*delta(Tj[0]-Tk[0])*flambda(Ti[1]+Tj[1]+Tk[1])
                if val != 0.:
                    val = val * (vb1**2/(vb1**2-1)-vb2**2/(vb2**2-1))
            elif atypes[i]=='K' and atypes[j]=='K' and atypes[k]=='L':
                vs1 = S1(Tj[1],Tk[1],Tj[0],Tk[0])
                vs2 = S2(Tj[1],Tk[1],Tj[0],Tk[0])
                val = vs1 * (delta(Ti[0]-Tk[0]-Tj[0])*delta(Ti[1]-Tk[1]+Tj[1])-
                delta(Ti[0]-Tk[0]-Tj[0])*delta(Ti[1]+Tk[1]-Tj[1])+(delta(Tk[0]-Tj[0]+Ti[0])+
                delta(Tk[0]-Tj[0]-Ti[0]))* delta(Tk[1] + Tj[1] - Ti[1]))+vs2*(
                delta(Ti[0] - Tk[0] - Tj[0]) * delta(Ti[1] - Tk[1] - Tj[1]) + 
                (delta(Tk[0] - Tj[0] - Ti[0]) + delta(Ti[0] + Tk[0] - Tj[0])) *(
                delta(Ti[1] - Tk[1] + Tj[1]) - delta(Tk[1] - Tj[1] + Ti[1])))
            val = val*n
            if val!=0.:
                TensorAtm['g'][i,j,k] = val
                TensorAtm['g'][j,k,i] = val
                TensorAtm['g'][k,i,j] = val
                TensorAtm['g'][i,k,j] = -val
                TensorAtm['g'][j,i,k] = -val
                TensorAtm['g'][k,j,i] = -val

for i in range(0,natm):
    for j in range(i,natm):
        for k in range(j,natm):
            Ti = awavenum[i]
            Tj = awavenum[j]
            Tk = awavenum[k]
            val=0.
            if atypes[i]=='L' and atypes[j]=='L' and atypes[k]=='L':
                vs3 = S3(Tj[1],Tk[1],Tj[0],Tk[0])
                vs4 = S4(Tj[1],Tk[1],Tj[0],Tk[0])
                val = vs3 * ((delta(Tk[0] - Tj[0] - Ti[0]) - delta(Tk[0]- Tj[0] + Ti[0])
                ) * delta(Tk[1] + Tj[1] - Ti[1]) + delta(Tk[0] + Tj[0] - Ti[0]) * (
                delta(Tk[1] - Tj[1]+ Ti[1]) - delta(Tk[1] - Tj[1] - Ti[1]))) + vs4 * (
                (delta(Tk[0] + Tj[0] - Ti[0]) * delta(Tk[1] - Tj[1] - Ti[1])) + (
                delta(Tk[0] - Tj[0] + Ti[0]) - delta(Tk[0] - Tj[0] - Ti[0])) * (
                delta(Tk[1] - Tj[1] - Ti[1]) - delta(Tk[1] - Tj[1] + Ti[1])))
            val = val*n
            if val!=0.:
                TensorAtm['g'][i,j,k]=val
                TensorAtm['g'][j,k,i]=val
                TensorAtm['g'][k,i,j]=val
                TensorAtm['g'][i,k,j]=-val
                TensorAtm['g'][j,i,k]=-val
                TensorAtm['g'][k,j,i]=-val

# TENSOR b; b(i,j)=(F_i, J(F_j, \nabla^2 F_k))
for i in range(0,natm):
    for j in range(0,natm):
        for k in range(0,natm):
            TensorAtm['b'][i,j,k] = TensorAtm['a'][k,k]*TensorAtm['g'][i,j,k]
            
# TENSOR c; c_{i,j} = (F_i, \partial_x F_j)
for i in range(0,natm):
    for j in range(0,natm):
        Ti = awavenum[i]
        Tj = awavenum[j]
        val = 0.
        if atypes[i]=='K' and atypes[j]=='L':
            val = n*Ti[0]*delta(Ti[0]-Tj[0])*delta(Ti[1]-Tj[1])
        if val != 0.:
            TensorAtm['c'][i,j]=val
            TensorAtm['c'][j,i]=-val

# TENSOR s; s_{i,j} = (F_i, \eta_j)
for i in range(0,natm):
    for j in range(0,noc):
        Ti = awavenum[i]
        Dj = owavenum[j]
        val=0.
        if atypes[i]=='A':
            val = flambda(Dj[0])*flambda(Dj[1]+Ti[1])
            if val!=0.:
                val = val*8.*np.sqrt(2.)*Dj[1]/(np.pi**2*(Dj[1]**2-Ti[1]**2)*Dj[0])
        elif atypes[i]=='K':
            val = flambda(2.*Ti[0]+Dj[0])*delta(Dj[1]-Ti[1])
            if val!=0.:
                val=val*4.*Dj[0]/(np.pi*(-4.*Ti[0]**2+Dj[0]**2))
        elif atypes[i]=='L':
            val = delta(Dj[1]-Ti[1])*delta(2*Ti[0]-Dj[0])
        if val!=0.:
            TensorAtm['s'][i,j]=val
            
# --------------------------------------------------------------------------- #
# OCEAN EQUATION INNER PRODUCTS
# --------------------------------------------------------------------------- #
# TENSOR K; K_{i,j} = (\eta_i, \nabla^2 F_j), forcing atm on ocean
for i in range(0,noc):
    for j in range(0,natm):
        TensorOc['K'][i,j]=TensorAtm['s'][j,i]*TensorAtm['a'][j,j]

# TENSOR M; M_{i,j} = (eta_i, \nabla^2 \eta_j), forcing ocean on ocean
for i in range(0,noc):
    Di = owavenum[i]
    TensorOc['M'][i,i]=-(n**2)*(Di[0]/2.)**2-Di[1]**2

# TENSOR N; N_{i,j} = (eta_i, \partial_x \eta_j), beta term for ocean
for i in range(0,noc):
    for j in range(0,noc):
        Di = owavenum[i]
        Dj = owavenum[j]
        val = delta(Di[1]-Dj[1])*flambda(Di[0]+Dj[0])
        if val != 0.:
            TensorOc['N'][i,j]=val*(-2)*Dj[0]*Di[0]*n/((Dj[0]**2-Di[0]**2)*np.pi)
            
# TENSOR O; O_{i,j,k} = (eta_i, J(\eta_j, \eta_k)), Temperature advection term (passive scalar)
for i in range(0,noc):
    for j in range(i,noc):
        for k in range(i,noc):
            Di = owavenum[i]
            Dj = owavenum[j]
            Dk = owavenum[k]
            vs3 = S3(Dj[1],Dk[1],Dj[0],Dk[0])
            vs4 = S4(Dj[1],Dk[1],Dj[0],Dk[0])
            val = vs3*((delta(Dk[0]-Dj[0]-Di[0])-delta(Dk[0]-Dj[0]+Di[0])
            )*delta(Dk[1]+Dj[1]-Di[1])+delta(Dk[0]+Dj[0]-Di[0])*(delta(Dk[1]-Dj[1]+Di[1])-
            delta(Dk[1]-Dj[1]-Di[1])))+vs4*((delta(Dk[0]+Dj[0]-Di[0])*
            delta(Dk[1]-Dj[1]-Di[1]))+(delta(Dk[0]-Dj[0]+Di[0])-delta(Dk[0]-Dj[0]-Di[0]))
            *(delta(Dk[1]-Dj[1]-Di[1])-delta(Dk[1]-Dj[1]+Di[1])))
            val = val*n/2.
            if val!=0.:
                TensorOc['O'][i,j,k] = val
                TensorOc['O'][j,k,i] = val
                TensorOc['O'][k,i,j] = val
                TensorOc['O'][i,k,j] = -val
                TensorOc['O'][j,i,k] = -val
                TensorOc['O'][k,j,i] = -val
          
# TENSOR C_oc; C_{i,j,k} = (\eta_i, J(\eta_j,\nabla^2 \eta_k))
for i in range(0,noc):
    for j in range(0,noc):
        for k in range(0,noc):
            val = TensorOc['M'][k,k]*TensorOc['O'][i,j,k]
            if val!=0.:
                TensorOc['C'][i,j,k]=val
            
# TENSOR W; W_{i,j} = (\eta_i, F_j), SWR forcing of ocean
for i in range(0,noc):
    for j in range(0,natm):
        TensorOc['W'][i,j]=TensorAtm['s'][j,i]
        
# --------------------------------------------------------------------------- #
# LAST ATMOSPHERIC THAT NEEDS OCEAN TENSOR
# --------------------------------------------------------------------------- #
        
# TENSOR d; d_{i,j} = (F_i, \nabla^2 \eta_j)
for i in range(0,natm):
    for j in range(0,noc):
        TensorAtm['d'][i,j]=TensorAtm['s'][i,j]*TensorOc['M'][j,j]