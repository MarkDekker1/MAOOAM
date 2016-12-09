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
#file1 = './mean_field_Co100.dat'
file2 = './evol_field_Co350.dat'

#open1=open(file1,'r')
open2=open(file2,'r')

#read1=open1.readlines()
read2=open2.readlines()

# TIME EVOLUTION
time=[]
Vpsi_a=[]
Vpsi_o=[]
Vtheta_a=[]
VdT_o=[]
for i in range(0,len(read2)):
    data=read2[i].split()
    time.append(data[0])
    Vpsi_a.append(data[1:11])
    Vtheta_a.append(data[11:21])
    Vpsi_o.append(data[21:29])
    VdT_o.append(data[29:38])
Vpsi_a=np.transpose(Vpsi_a).astype(np.float)
Vtheta_a=np.transpose(Vtheta_a).astype(np.float)
Vpsi_o=np.transpose(Vpsi_o).astype(np.float)
VdT_o=np.transpose(VdT_o).astype(np.float)
times=np.array(time).astype(np.float)

# MEAN FIELD
#Mpsi_a=read1[0].split()[1:11]
#Mtheta_a=read1[0].split()[11:21]
#Mpsi_o=read1[0].split()[21:29]
#MdT_o=read1[0].split()[29:38]

#%%std, Co100
V1_1=Vpsi_a
V1_2=Vpsi_o
V1_3=Vtheta_a
V1_4=VdT_o
#%%std, Co200
V2_1=Vpsi_a
V2_2=Vpsi_o
V2_3=Vtheta_a
V2_4=VdT_o
#%%std, Co350
V3_1=Vpsi_a
V3_2=Vpsi_o
V3_3=Vtheta_a
V3_4=VdT_o

#%%d1e9
V1_1=Vpsi_a
V1_2=Vpsi_o
V1_3=Vtheta_a
V1_4=VdT_o

#%%d5e9
V2_1=Vpsi_a
V2_2=Vpsi_o
V2_3=Vtheta_a
V2_4=VdT_o


#%%d1e8
V3_1=Vpsi_a
V3_2=Vpsi_o
V3_3=Vtheta_a
V3_4=VdT_o

#%%d5e8
V4_1=Vpsi_a
V4_2=Vpsi_o
V4_3=Vtheta_a
V4_4=VdT_o


#%%d1e7
V5_1=Vpsi_a
V5_2=Vpsi_o
V5_3=Vtheta_a
V5_4=VdT_o
