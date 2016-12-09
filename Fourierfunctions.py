# RECOMPOSE FOURIER MODES
def Fa(x,y,Nx,Ny):
    return np.sqrt(2.)*np.cos(Ny*y)
def Fk(x,y,Nx,Ny):
    return 2.*np.cos(Nx*x)*np.sin(Ny*y)
def Fl(x,y,Nx,Ny):
    return 2.*np.sin(Nx*n*x/2.)*np.sin(Ny*y)
def Phi(x,y,Nx,Ny):
    return 2.*np.sin(Nx*n*x/2.)*np.sin(Ny*y)
def MPhi(Nx,Ny):
    if np.mod(Nx,2)==1 and np.mod(Ny,2)==1:
        return 2.*((-1.)**Nx-1.)*((-1.)**Ny-1.)/(Nx*Ny*np.pi**2.)
    else:
        return 0.

# ADDING FOURIER MODES
def Psi_a(x,y,t):
    C1=Fa(x,y,0,1)*Vpsi_a[0][t]
    C2=Fk(x,y,1,1)*Vpsi_a[1][t]
    C3=Fl(x,y,1,1)*Vpsi_a[2][t]
    C4=Fa(x,y,0,2)*Vpsi_a[3][t]
    C5=Fk(x,y,1,2)*Vpsi_a[4][t]
    C6=Fl(x,y,1,2)*Vpsi_a[5][t]
    C7=Fk(x,y,2,1)*Vpsi_a[6][t]
    C8=Fl(x,y,2,1)*Vpsi_a[7][t]
    C9=Fk(x,y,2,2)*Vpsi_a[8][t]
    C10=Fl(x,y,2,2)*Vpsi_a[9][t]
    return C1+C2+C3+C4+C5+C6+C7+C8+C9+C10
def dT_a(x,y,t):
    C1=Fa(x,y,0,1)*Vtheta_a[0][t]
    C2=Fk(x,y,1,1)*Vtheta_a[1][t]
    C3=Fl(x,y,1,1)*Vtheta_a[2][t]
    C4=Fa(x,y,0,2)*Vtheta_a[3][t]
    C5=Fk(x,y,1,2)*Vtheta_a[4][t]
    C6=Fl(x,y,1,2)*Vtheta_a[5][t]
    C7=Fk(x,y,2,1)*Vtheta_a[6][t]
    C8=Fl(x,y,2,1)*Vtheta_a[7][t]
    C9=Fk(x,y,2,2)*Vtheta_a[8][t]
    C10=Fl(x,y,2,2)*Vtheta_a[9][t]
    return 2.*f0/R*(C1+C2+C3+C4+C5+C6+C7+C8+C9+C10)
def Psi_o(x,y,t):
    C1=(Phi(x,y,1,1)-MPhi(1,1))*Vpsi_o[0][t]
    C2=(Phi(x,y,1,2)-MPhi(1,2))*Vpsi_o[1][t]
    C3=(Phi(x,y,1,3)-MPhi(1,3))*Vpsi_o[2][t]
    C4=(Phi(x,y,1,4)-MPhi(1,4))*Vpsi_o[3][t]
    C5=(Phi(x,y,2,1)-MPhi(2,1))*Vpsi_o[4][t]
    C6=(Phi(x,y,2,2)-MPhi(2,2))*Vpsi_o[5][t]
    C7=(Phi(x,y,2,3)-MPhi(2,3))*Vpsi_o[6][t]
    C8=(Phi(x,y,2,4)-MPhi(2,4))*Vpsi_o[7][t]
    return C1+C2+C3+C4+C5+C6+C7+C8
def dT_o(x,y,t):
    C1=Phi(x,y,1,1)*VdT_o[0][t]
    C2=Phi(x,y,1,2)*VdT_o[1][t]
    C3=Phi(x,y,1,3)*VdT_o[2][t]
    C4=Phi(x,y,1,4)*VdT_o[3][t]
    C5=Phi(x,y,2,1)*VdT_o[4][t]
    C6=Phi(x,y,2,2)*VdT_o[5][t]
    C7=Phi(x,y,2,3)*VdT_o[6][t]
    C8=Phi(x,y,2,4)*VdT_o[7][t]
    return C1+C2+C3+C4+C5+C6+C7+C8
def Psi_a1(x,y,t): #Zonal atmospheric jet
    C1=Fa(x,y,0,1)*Vpsi_a[0][t]
    return C1
def dT_a1(x,y,t): #Meridional T distribution
    C1=Fa(x,y,0,1)*Vtheta_a[0][t]
    return C1
def Psi_o2(x,y,t): # Gulf stream
    C2=(Phi(x,y,1,2)-MPhi(1,2))*Vpsi_o[1][t]
    return C2
def dT_o2(x,y,t): # T anomaly ocean
    C2=Phi(x,y,1,2)*VdT_o[1][t]
    return C2

# FIELD AT TIME t
yvec=np.arange(0,np.pi,0.01)
xvec=np.arange(0,2*np.pi/n,0.01)
def Field(var,t,sp):
    field=[]
    if sp == 0:
        if var=='psia':
            for x in xvec:
                field.append(Psi_a(x,yvec,t))
        if var=='psio':
            for x in xvec:
                field.append(Psi_o(x,yvec,t))
        if var=='dTa':
            for x in xvec:
                field.append(dT_a(x,yvec,t))
        if var=='dTo':
            for x in xvec:
                field.append(dT_o(x,yvec,t))
    if sp == 1:
        if var=='psia':
            for x in xvec:
                field.append(Psi_a1(x,yvec,t))
        if var=='psio':
            for x in xvec:
                field.append(Psi_o2(x,yvec,t))
        if var=='dTa':
            for x in xvec:
                field.append(dT_a1(x,yvec,t))
        if var=='dTo':
            for x in xvec:
                field.append(dT_o2(x,yvec,t))
    return np.transpose(field)
def Field_up(var,t):
    field=[]
    if var=='psia':
        for y in yvec:
            field.append(Psi_a(xvec,y,t))
    if var=='psio':
        for y in yvec:
            field.append(Psi_o(xvec,y,t))
    if var=='dTa':
        for y in yvec:
            field.append(dT_a(xvec,y,t))
    if var=='dTo':
        for y in yvec:
            field.append(dT_o(xvec,y,t))
    return field[np.int(len(yvec)/2):]
def Field_down(var,t):
    field=[]
    if var=='psia':
        for y in yvec:
            field.append(Psi_a(xvec,y,t))
    if var=='psio':
        for y in yvec:
            field.append(Psi_o(xvec,y,t))
    if var=='dTa':
        for y in yvec:
            field.append(dT_a(xvec,y,t))
    if var=='dTo':
        for y in yvec:
            field.append(dT_o(xvec,y,t))
    return field[0:np.int(len(yvec)/2)]