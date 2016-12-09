#%%
# --------------------------------------------------------------------------- #
# Stability diagram with dp
# --------------------------------------------------------------------------- #

PCargs = args(name='EQ1', type='EP-C',force=True)  # 'EP-C' stands for Equilibrium Point Curve. The branch will be labeled 'EQ1'.
PCargs.freepars     = ['dp']                      # control parameter(s) (it should be among those specified in DSargs.pars)
PCargs.MaxNumPoints = 50                        # The following 3 parameters are set after trial-and-error
PCargs.MaxStepSize  = 1e-4
PCargs.MinStepSize  = 1e-7
PCargs.StepSize     = 2e-5
PCargs.LocBifPoints = 'all'                       # detect limit points / saddle-node bifurcations
PCargs.SaveEigen    = True                       # to tell unstable from stable branches


plt.figure()
a=PC.newCurve(PCargs)
print 'Computing forward...'
PC['EQ1'].forward()
print 'done in %.3f seconds!' % (clock()-start)
#%%
# --------------------------------------------------------------------------- #
# Stability diagram with SWR
# --------------------------------------------------------------------------- #

PCargs = args(name='EQ2', type='EP-C',force=True)  # 'EP-C' stands for Equilibrium Point Curve. The branch will be labeled 'EQ1'.
PCargs.freepars     = ['SWR']                      # control parameter(s) (it should be among those specified in DSargs.pars)
PCargs.MaxNumPoints = 1000                        # The following 3 parameters are set after trial-and-error
PCargs.MaxStepSize  = 1e1
PCargs.MinStepSize  = 1e-2
PCargs.StepSize     = 2e-1
PCargs.LocBifPoints = 'all'                       # detect limit points / saddle-node bifurcations
PCargs.SaveEigen    = True                       # to tell unstable from stable branches


plt.figure()
a=PC.newCurve(PCargs)
print 'Computing forward...'
PC['EQ2'].forward()
print 'done in %.3f seconds!' % (clock()-start)

#%%
# --------------------------------------------------------------------------- #
# Run 2
# --------------------------------------------------------------------------- #

PCargs = args(name='EQ3', type='FP-C',force=True)  # 'EP-C' stands for Equilibrium Point Curve. The branch will be labeled 'EQ1'.
#PCargs.initpoint    = 'EQ1:P1'

PCargs.freepars     = ['SWR','dp']                      # control parameter(s) (it should be among those specified in DSargs.pars)
PCargs.MaxNumPoints = 100                        # The following 3 parameters are set after trial-and-error
PCargs.MaxStepSize  = 1e-0
PCargs.MinStepSize  = 1e-4
PCargs.StepSize     = 2e-1
PCargs.LocBifPoints = 'all'                       # detect limit points / saddle-node bifurcations
PCargs.SaveEigen    = True                       # to tell unstable from stable branches

plt.figure()
a=PC.newCurve(PCargs)
print 'Computing forward...'
PC['EQ3'].forward()
print 'done in %.3f seconds!' % (clock()-start)

#%%
fig=plt.figure(figsize=(10,6))
data=PC.display(['SWR','X1'], stability=True,figure=3,linewidth=2)        # stable and unstable branches as solid and dashed curves, resp.
plt.ylabel('X1',fontsize=15)
#plt.ylim([1,3.5])
plt.xlabel(r'dp',fontsize=15)
#plt.xlim([1e-10,1e-3])
plt.xscale('log')
plt.title('')
plt.show()
