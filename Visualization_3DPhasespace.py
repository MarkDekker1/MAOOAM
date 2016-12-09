
# PHASE SPACE
Xvec=Vpsi_o[1]
Yvec=VdT_o[1]
Zvec=Vpsi_a[0]
T0=4000


fig = plt.figure(figsize=(8,6))
ax = fig.gca(projection='3d')
ax.view_init(azim=-60)
ax.plot(Xvec[T0:],Yvec[T0:],Zvec[T0:],'r')
        
ax.set_xlabel(r'$\psi_{o,1}$',fontsize=15)
ax.set_ylabel(r'$\theta_{o,1}$',fontsize=15)
ax.set_zlabel(r'$\psi_{a,0}$',fontsize=15)
ax.tick_params(axis='both',which='major',labelsize=10)

plt.show()
