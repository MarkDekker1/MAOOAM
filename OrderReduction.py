# --------------------------------------------------------------------------- #
# Reduce model order
# --------------------------------------------------------------------------- #
ToKeep = [0,1,10,11,20,21,28,29]
pars={}
for i in range(0,36):
    if i not in ToKeep:
        del DSargs.varspecs[AllVars[i]]
        del icdict[AllVars[i]]
        pars[AllVars[i]]=0
SWR=1
pars['rp']=rp
pars['dp0']=dp
pars['dp']=dp
pars['Cpo0']=Cpo
pars['Cpa0']=Cpa
pars['SWR']=SWR