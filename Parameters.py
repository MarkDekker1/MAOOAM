# --------------------------------------------------------------------------- #
# CODE MAOOAM IN PYTHON
# --------------------------------------------------------------------------- #
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from scipy.stats import gaussian_kde
import time as T

# --------------------------------------------------------------------------- #
# PHYSICAL PARAMETERS
# --------------------------------------------------------------------------- #
# OCEAN AND ATMOSPHERE
scale = 5e6       #  the characteristic space scale, L*pi
f0 = 1.032e-4     #  Coriolis parameter at 45 degrees latitude	
n = 1.5e0         #  aspect ratio (n = 2Ly/Lx ; Lx = 2*pi*L/n; Ly = pi*L)
rra = 6370e3      #  earth radius	
phi0_npi = 0.25e0 #  latitude exprimed in fraction of pi

# OCEAN
gp = 3.1e-2       #  reduced gravity
r = 1e-8          #  frictional coefficient at the bottom of the ocean	
H = 5e2           #  depth of the water layer of the ocean
#d = 1e-8          #  the coupling parameter (should be divided by f0 in order to be adimensional)

# ATMOSPHERE
k = 0.02e0        #  atmosphere bottom friction coefficient
kp = 0.04e0       #  atmosphere internal friction coefficient
sig0 = 0.1e0      #  static stability of the atmosphere

# T-RELATED OCEAN
Go = 2e8          #  Specific heat capacity of the ocean (50m layer)
#Co = 350.        #  Constant short-wave radiation of the ocean
To0 = 285e0       #  Stationary solution for the 0-th order ocean temperature

# T-RELATED ATMOSPHERE
Ga = 1e7          #  Specific heat capacity of the atmosphere
#Ca = Co/4.       #  Constant short-wave radiation of the atmosphere
epsa = 0.76e0     #  Emissivity coefficient for the grey-body atmosphere
Ta0 = 270e0       #  Stationary solution for the 0-th order atmospheric temperature

# OTHER T-RELATED
sc = 1e0          #  Ratio of surface to atmosphere temperature
#lda = 20e0        #  Sensible + turbulent heat exchange between ocean and atmosphere
RR = 287e0        #  Gas constant of dry air
sB = 5.6e-8       #  Stefan-Boltzmann constant

# --------------------------------------------------------------------------- #
# NUMERICAL PARAMETERS
# --------------------------------------------------------------------------- #
t_trans = 0    #  transient period (e.g. 1.D7)
t_run = 100       #  length of trajectory on the attractor (e.g. 5.D8)
dt = 1e-2         #  the time step
writeout0 = 1      #  write out all variables every tw time units
TW = 1e1         #

# --------------------------------------------------------------------------- #
# FOURIER MODE SELECTION
# --------------------------------------------------------------------------- #
nboc = 8          #  Number of oceanic blocs
nbatm = 4         #  Number of atmospheric blocs

oms = np.zeros(shape=(8,2))
oms[0,:] = 1,1
oms[1,:] = 1,2
oms[2,:] = 1,3
oms[3,:] = 1,4
oms[4,:] = 2,1
oms[5,:] = 2,2
oms[6,:] = 2,3
oms[7,:] = 2,4

ams = np.zeros(shape=(4,2))
ams[0,:] = 1,1
ams[1,:] = 1,2
ams[2,:] = 2,1
ams[3,:] = 2,2

# --------------------------------------------------------------------------- #
# DIMENSION CALCULATION
# --------------------------------------------------------------------------- #
natm=0
for i in range(0,nbatm):
    if ams[i,1]==1:
        natm=natm+3
    else:
        natm=natm+2
s=len(oms)
noc=s

ndim=2*natm+2*noc

# --------------------------------------------------------------------------- #
# GENERAL PARAMETERS
# --------------------------------------------------------------------------- #
pi=np.pi
L=scale/pi
phi0=phi0_npi*pi
LR=np.sqrt(gp*H)/f0
G=-L**2/LR**2
betp=L/rra*np.cos(phi0)/np.sin(phi0)
rp=r/f0
#dp=d/f0
kd=k*2
kdp=kp

# --------------------------------------------------------------------------- #
# DERIVED QUANTITIES
# --------------------------------------------------------------------------- #
#Cpo=Co/(Go*f0) * RR/(f0**2*L**2)
#Lpo=lda/(Go*f0)
#Cpa=Ca/(Ga*f0) * RR/(f0**2*L**2)/2  # Cpa acts on psi1-psi3, not on theta
#Lpa=lda/(Ga*f0)
sBpo=4*sB*To0**3/(Go*f0)            # long wave radiation lost by ocean to atmosphere space
sBpa=8*epsa*sB*Ta0**3/(Go*f0)       # long wave radiation from atmosphere absorbed by ocean
LSBpo=2*epsa*sB*To0**3/(Ga*f0)      # long wave radiation from ocean absorbed by atmosphere
LSBpa=8*epsa*sB*Ta0**3/(Ga*f0)      # long wave radiation lost by atmosphere to space & ocea

# --------------------------------------------------------------------------- #
# DERIVED QUANTITIES
# --------------------------------------------------------------------------- #
IC=np.zeros(ndim)
# PSI VARIABLES
IC[0] = 0e0   # typ= A, Nx= 0.0, Ny= 1.0
IC[1] = 0e0   # typ= K, Nx= 1.0, Ny= 1.0
IC[2] = 0e0   # typ= L, Nx= 1.0, Ny= 1.0
IC[3] = 0e0   # typ= A, Nx= 0.0, Ny= 2.0
IC[4] = 0e0   # typ= K, Nx= 1.0, Ny= 2.0
IC[5] = 0e0   # typ= L, Nx= 1.0, Ny= 2.0
IC[6] = 0e0   # typ= K, Nx= 2.0, Ny= 1.0
IC[7] = 0e0   # typ= L, Nx= 2.0, Ny= 1.0
IC[8] = 0e0   # typ= K, Nx= 2.0, Ny= 2.0
IC[9] = 0e0   # typ= L, Nx= 2.0, Ny= 2.0

# THETA VARIABLES
IC[10] = 0e0  # typ= A, Nx= 0.0, Ny= 1.0
IC[11] = 0e0  # typ= K, Nx= 1.0, Ny= 1.0
IC[12] = 0e0  # typ= L, Nx= 1.0, Ny= 1.0
IC[13] = 0e0  # typ= A, Nx= 0.0, Ny= 2.0
IC[14] = 0e0  # typ= K, Nx= 1.0, Ny= 2.0
IC[15] = 0e0  # typ= L, Nx= 1.0, Ny= 2.0
IC[16] = 0e0  # typ= K, Nx= 2.0, Ny= 1.0
IC[17] = 0e0  # typ= L, Nx= 2.0, Ny= 1.0
IC[18] = 0e0  # typ= K, Nx= 2.0, Ny= 2.0
IC[19] = 0e0  # typ= L, Nx= 2.0, Ny= 2.0
 
# A VARIABLES
IC[20] = 0e0  # Nx= 0.5, Ny= 1.0
IC[21] = 0e0  # Nx= 0.5, Ny= 2.0
IC[22] = 0e0  # Nx= 0.5, Ny= 3.0
IC[23] = 0e0  # Nx= 0.5, Ny= 4.0
IC[24] = 0e0  # Nx= 1.0, Ny= 1.0
IC[25] = 0e0  # Nx= 1.0, Ny= 2.0
IC[26] = 0e0  # Nx= 1.0, Ny= 3.0
IC[27] = 0e0  # Nx= 1.0, Ny= 4.0

# T VARIABLES
IC[28] = 0e0  # Nx= 0.5, Ny= 1.0
IC[29] = 0e0  # Nx= 0.5, Ny= 2.0
IC[30] = 0e0  # Nx= 0.5, Ny= 3.0
IC[31] = 0e0  # Nx= 0.5, Ny= 4.0
IC[32] = 0e0  # Nx= 1.0, Ny= 1.0
IC[33] = 0e0  # Nx= 1.0, Ny= 2.0
IC[34] = 0e0  # Nx= 1.0, Ny= 3.0
IC[35] = 0e0  # Nx= 1.0, Ny= 4.0