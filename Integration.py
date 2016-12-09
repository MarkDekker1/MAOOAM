#%%
# --------------------------------------------------------------------------- #
# Integration of the ODE system - Python way
# --------------------------------------------------------------------------- #
    
t = np.arange(0,100000,10)
X0=np.zeros(36)

print 'Computing Integration...'
start = clock()
Results, infodict = integrate.odeint(Equations, X0, t, full_output=True)
print 'done in %.3f seconds!' % (clock()-start)
X1,X2,X3,X4,X5,X6,X7,X8,X9,X10,X11,X12,X13,X14,X15,X16,X17,X18,X19,X20,X21,X22,X23,X24,X25,X26,X27,X28,X29,X30,X31,X32,X33,X34,X35,X36=Results.T

#%%
# --------------------------------------------------------------------------- #
# Integration of the ODE system - read fortran data
# --------------------------------------------------------------------------- #

X1,X2,X3,X4,X5,X6,X7,X8,X9,X10=Vpsi_a
X11,X12,X13,X14,X15,X16,X17,X18,X19,X20=Vtheta_a
X21,X22,X23,X24,X25,X26,X27,X28=Vpsi_o
X29,X30,X31,X32,X33,X34,X35,X36=VdT_o
t = times

#%%
# --------------------------------------------------------------------------- #
# Extract variances from Fortran data
# --------------------------------------------------------------------------- #
Var=[]
for i in range(0,10):
    Var.append(np.var(Vpsi_a[i]))
for i in range(0,10):
    Var.append(np.var(Vtheta_a[i]))
for i in range(0,8):
    Var.append(np.var(Vpsi_o[i]))
for i in range(0,8):
    Var.append(np.var(VdT_o[i]))

#%%
# --------------------------------------------------------------------------- #
# Integration of the SDE system - Python way (with noise!)
# --------------------------------------------------------------------------- #
import time

dt=10
tmax=1000000.
t = np.arange(0,tmax,dt)
X0=np.zeros(36)
Vx=np.zeros(shape=(np.int(tmax/dt),36))

def updateX():
    global X1,X2,X3,X4,X5,X6,X7,X8,X9,X10,X11,X12,X13,X14,X15,X16,X17,X18,X19,X20,X21,X22,X23,X24,X25,X26,X27,X28,X29,X30,X31,X32,X33,X34,X35,X36
    X1=X0[0]
    X2=X0[1]
    X3=X0[2]
    X4=X0[3]
    X5=X0[4]
    X6=X0[5]
    X7=X0[6]
    X8=X0[7]
    X9=X0[8]
    X10=X0[9]
    X11=X0[10]
    X12=X0[11]
    X13=X0[12]
    X14=X0[13]
    X15=X0[14]
    X16=X0[15]
    X17=X0[16]
    X18=X0[17]
    X19=X0[18]
    X20=X0[19]
    X21=X0[20]
    X22=X0[21]
    X23=X0[22]
    X24=X0[23]
    X25=X0[24]
    X26=X0[25]
    X27=X0[26]
    X28=X0[27]
    X29=X0[28]
    X30=X0[29]
    X31=X0[30]
    X32=X0[31]
    X33=X0[32]
    X34=X0[33]
    X35=X0[34]
    X36=X0[35]

def kvec():
    K=np.zeros(36)
    for k in range(0,36):
        K[k]=dt*eval(EQNS[AllVars[k]])
    return K    
    
def Noise():
    N=np.zeros(36)
    for n in range(0,36):
        if Var[n]>0:
            N[n]=np.random.normal(0,Var[n]/2.)
        else:
            N[n]=0
    return N    
    
print 'Computing Integration...'
start = time.clock()
for i in t:
    Xold=X0
    
    updateX()
#    Vx1.append(X1)
#    Vx2.append(X11)
#    Vx3.append(X22)
#    Vx4.append(X30)
    Vx[np.int(i/10.)]=X0
    k1=kvec() 
    
    X0=Xold+0.5*k1
    updateX()
    k2=kvec()   
    
    X0=Xold+0.5*k2
    updateX()
    k3=kvec()
    
    X0=Xold+k3
    updateX()
    k4=kvec()
    
    #X0=Xold*(1+np.random.normal(0,0.05))+1./6.*(k1+2*k2+2*k3+k4)
    X0=Xold+1./6.*(k1+2*k2+2*k3+k4)#+Noise()
    
    if np.mod(i,np.int(tmax/100.))==0:
        print str(i/tmax*100.)+' % complete'
    
print 'done in %.3f seconds!' % (clock()-start)