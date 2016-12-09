
from PyDSTool import *
from AOTensor import *
from Parameters import *
from Setup import *
from OrderReduction import *
import matplotlib.pyplot as plt

# --------------------------------------------------------------------------- #
# Set up ODE system
# --------------------------------------------------------------------------- #

EQNS=CreateEquations_general()
icdict=InitialConditions(0.0)
Seppars={'d':1e-9,'lda':20,'Co':150}
extrapars={}
#EQNS,icdict,extrapars=Reductor(4,EQNS,icdict,extrapars)
Seppars.update(extrapars) # only for case reduced order
DSargs = args(name='MAOOAM')
DSargs.varspecs=EQNS
DSargs.ics=icdict
DSargs.pars = Seppars
DSargs.tdomain = [0,50]

ode  = Generator.Vode_ODEsystem(DSargs)
#ode.xdomain={'X1':[-0.01,0.05],'X2':[-1,1],'X11':[-1,1],'X12':[-0.002,0.002],'X22':[0,0.2]}

# --------------------------------------------------------------------------- #
# Set up continuation class
# --------------------------------------------------------------------------- #

PC = ContClass(ode)

#%%
# --------------------------------------------------------------------------- #
# RUN: MOMENTUM COUPLING
# --------------------------------------------------------------------------- #

PCargs = args(name='EQ_d', type='EP-C',force=True)
PCargs.freepars     = ['d']
PCargs.MaxNumPoints = 75
PCargs.MaxStepSize  = 1e1
PCargs.MinStepSize  = 1e-8
PCargs.StepSize     = 2e-8
PCargs.verbosity = 2
PCargs.LocBifPoints = 'all'
PCargs.SaveEigen    = True
a=PC.newCurve(PCargs)

print 'Computing forward...'
start = clock()
PC['EQ_d'].forward()
print 'done in %.3f seconds!' % (clock()-start)

#print 'Computing backward...'
#start = clock()
#PC['EQ_d'].backward()
#print 'done in %.3f seconds!' % (clock()-start)

data=PC['EQ_d'].display(['d','X1'], stability=True, figure=3,linewidth=2)
plt.ylabel(r'$\psi_a (0)$',fontsize=15)
plt.xlabel(r'Momentum coupling $d$',fontsize=15)
plt.title('')
y_formatter = plty.ticker.ScalarFormatter(useOffset=False)
plt.show()

#%%
# --------------------------------------------------------------------------- #
# RUN: SOLAR IRRADIANCE
# --------------------------------------------------------------------------- #

PCargs = args(name='EQ_co', type='EP-C',force=True)
PCargs.freepars     = ['Co']
PCargs.MaxNumPoints = 50
PCargs.MaxStepSize  = 1e1
PCargs.MinStepSize  = 1e-1
PCargs.StepSize     = 1e0
PCargs.verbosity = 2
PCargs.LocBifPoints = 'all'
PCargs.SaveEigen    = True
a=PC.newCurve(PCargs)

print 'Computing forward...'
start = clock()
PC['EQ_co'].forward()
print 'done in %.3f seconds!' % (clock()-start)

#print 'Computing backward...'
#start = clock()
#PC['EQ_co'].backward()
#print 'done in %.3f seconds!' % (clock()-start)

plt.figure()
data=PC['EQ_co'].display(['Co','X1'], stability=True, figure=3,linewidth=2)
plt.ylabel(r'$\psi_a (0)$',fontsize=15)
plt.xlabel(r'Solar irradiance $C_o$',fontsize=15)
plt.title('')
plt.show()
#%%
# --------------------------------------------------------------------------- #
# RUN: THERMAL COUPLING
# --------------------------------------------------------------------------- #

PCargs = args(name='EQ_lda', type='EP-C',force=True)
PCargs.freepars     = ['lda']
PCargs.MaxNumPoints = 100
PCargs.MaxStepSize  = 1e0
PCargs.MinStepSize  = 1e-4
PCargs.StepSize     = 2e-1
PCargs.verbosity = 2
PCargs.LocBifPoints = 'all'
PCargs.SaveEigen    = True
a=PC.newCurve(PCargs)

print 'Computing forward...'
start = clock()
PC['EQ_lda'].forward()
print 'done in %.3f seconds!' % (clock()-start)

#print 'Computing backward...'
#start = clock()
#PC['EQ_lda'].backward()
#print 'done in %.3f seconds!' % (clock()-start)
#%%
plt.figure()
data=PC['EQ_lda'].display(['lda','X11'], stability=True, figure=3,linewidth=2)
plt.ylabel(r'$\psi_a (0)$',fontsize=15)
plt.xlabel(r'Thermal coupling $\lambda$',fontsize=15)
plt.title('')
plt.show()