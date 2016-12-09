# READ MAOOAM
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from scipy.stats import gaussian_kde
import time as T

# IMPORTANT PARAMETERS
n=1.5
Omega=7.2921*10**(-5)
phi=45./360.*2.*np.pi
f0=np.sin(phi)*2.*Omega
R=287.

# DATA READ
#file1 = './mean_field_d1e7.dat'
#file1 = './evol_field_d1e9.dat'
#file2 = './evol_field_d5e9.dat'
#file3 = './evol_field_d1e8.dat'
#file4 = './evol_field_d5e8.dat'
#file5 = './evol_field_d1e7.dat'
file6 = './evol_field_Co100.dat'
file7 = './evol_field_Co150.dat'
file8 = './evol_field_Co200.dat'
file9 = './evol_field_Co250.dat'
file10 = './evol_field_Co300.dat'
file11 = './evol_field_Co350.dat'

files=[file6,file7,file8,file9,file10,file11]
Stability=[]
Limit=[]

Total=[]
for k in files:
    open1=open(k,'r')
    
    read1=open1.readlines()
    
    # TIME EVOLUTION
    Matrix=[]
    for i in range(8000,len(read1)):
        data=read1[i].split()
        Matrix.append(data[1:])
    Matrix=np.transpose(Matrix).astype(np.float)
    Total.append(Matrix)
    
    # Check if FP or LC (by checking X1):
    if (max(Matrix[0])-min(Matrix[0]))/min(Matrix[0])>0.5:
        Stability.append('LC')
#        summb=[]
#        for j in range(0,len(Matrix[0])-1):
#            summa=[]
#            for i in range(0,36):
#                summa.append(np.array(Matrix[i][j])*np.array(Matrix[i][j]))
#            summb.append(summb)
#            
#        summb=np.array(Matrix)
        Limit.append(1)
            
        
        
        
    else:
        Stability.append('FP')
        summy=[]
        for i in range(0,36):
            summy.append(np.array(Matrix[i][len(Matrix[0])-1])*np.array(Matrix[i][len(Matrix[0])-1]))
        Limit.append(sum(summy))