# --------------------------------------------------------------------------- #
# Whole horizontals
# --------------------------------------------------------------------------- #

t=1000
Nc=25

fig, ((ax1,ax2),(ax3,ax4)) = plt.subplots(2,2,sharex='col',sharey='row',figsize=(10,10))

ax1.contourf(xvec,yvec,Field('psia',t,0),Nc,cmap=plt.cm.seismic)
ax2.contourf(xvec,yvec,Field('psio',t,0),Nc,cmap=plt.cm.seismic)
ax3.contourf(xvec,yvec,Field('dTa',t,0),Nc,cmap=plt.cm.seismic)
ax4.contourf(xvec,yvec,Field('dTo',t,0),Nc,cmap=plt.cm.seismic)

ax1.set_title(r'$\Psi_a$',fontsize=15)
ax2.set_title(r'$\Psi_o$',fontsize=15)
ax3.set_title(r'$\delta T_a$',fontsize=15)
ax4.set_title(r'$\delta T_o$',fontsize=15)

ax1.tick_params(axis='both',which='major',labelsize=15)
ax3.tick_params(axis='both',which='major',labelsize=15)
ax4.tick_params(axis='both',which='major',labelsize=15)

plt.show()


#%%
# PLOT HORIZONTALS SPECIFICS
t=10000
Nc=25

fig, ((ax1,ax2),(ax3,ax4)) = plt.subplots(2,2,sharex='col',sharey='row',figsize=(10,10))

ax1.contourf(xvec,yvec,Field('psia',t,1),Nc,cmap=plt.cm.seismic)
ax2.contourf(xvec,yvec,Field('psio',t,1),Nc,cmap=plt.cm.seismic)
ax3.contourf(xvec,yvec,Field('dTa',t,1),Nc,cmap=plt.cm.seismic)
ax4.contourf(xvec,yvec,Field('dTo',t,1),Nc,cmap=plt.cm.seismic)

ax1.set_title(r'$\Psi_a$',fontsize=15)
ax2.set_title(r'$\Psi_o$',fontsize=15)
ax3.set_title(r'$\delta T_a$',fontsize=15)
ax4.set_title(r'$\delta T_o$',fontsize=15)

ax1.tick_params(axis='both',which='major',labelsize=15)
ax3.tick_params(axis='both',which='major',labelsize=15)
ax4.tick_params(axis='both',which='major',labelsize=15)

plt.show()
