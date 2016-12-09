
from PyDSTool import *
from AOTensor import *
from Parameters import *
from Setup import *

# --------------------------------------------------------------------------- #
# Set up ODE system
# --------------------------------------------------------------------------- #

EQNS=CreateEquations_general()

DSargs = args(name='MAOOAM')
DSargs.varspecs=EQNS
DSargs.ics=icdict
DSargs.pars = {'d':d,'lda':0,'Co':Co}
DSargs.tdomain = [0,50]

ode  = Generator.Vode_ODEsystem(DSargs)
ode.xdomain={'X1':[-0.01,0.05],'X2':[-1,1],'X11':[-1,1],'X12':[-0.002,0.002],'X22':[0,0.2]}

# --------------------------------------------------------------------------- #
# Set up continuation class
# --------------------------------------------------------------------------- #

PC = ContClass(ode)

# --------------------------------------------------------------------------- #
# Run forward equilibrium curve
# --------------------------------------------------------------------------- #

PCargs = args(name='EQ1', type='LC-C')
PCargs.freepars     = ['d']
PCargs.MaxNumPoints = 5
PCargs.MaxStepSize  = 1e-1
PCargs.MinStepSize  = 1e-4
PCargs.StepSize     = 2e-3
PCargs.LocBifPoints = 'all'
PCargs.SaveEigen    = True
a=PC.newCurve(PCargs)

print 'Computing curve...'
start = clock()
PC['EQ1'].forward()
print 'done in %.3f seconds!' % (clock()-start)
#%%
# --------------------------------------------------------------------------- #
# CREATE BIFURCATION DIAGRAM
# --------------------------------------------------------------------------- #
plt.figure()
data=PC['EQ1'].display(['d','X1'], stability=True, figure=3,linewidth=2)        # stable and unstable branches as solid and dashed curves, resp.
plt.ylabel(r'$\psi_a (0)$',fontsize=15)
#plt.ylim([1,3.5])
plt.xlabel(r'Coupling parameter $d$',fontsize=15)
#plt.xlim([0,2])
plt.title('')
plt.show()