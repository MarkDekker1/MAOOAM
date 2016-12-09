# PROB DENSITY
X1=3.2
Y1=2.5
X2=1
Y2=2.5
X3=3.2
Y3=0.75
X4=1
Y4=0.75
Nc=25
Time=np.linspace(0,99999,100000).astype(np.int)
T0=99000
Vector=Psi_a(X1,Y1,Time[T0:])
Vector=Psi_o(X1,Y1,Time[T0:])
Vector=dT_a(X1,Y1,Time[T0:])
Vector=dT_o(X4,Y4,Time[T0:])

Vector=[]
for t in Time[T0:]:
    Vector.append(np.mean(Field_down('psia',t))-np.mean(Field_up('psia',t))) # Zonal wind jet

fig = plt.figure(figsize=(8,4))
density = gaussian_kde(Vector1)
xs = np.linspace(np.min(Vector1),np.max(Vector1),500)
density.covariance_factor = lambda : 0.05
density._compute_covariance()
plt.plot(xs,density(xs),linewidth=3)
plt.xlabel(r'Value $y$',fontsize=15)
plt.ylabel(r'Probability density $p(y)$',fontsize=15)
plt.tick_params(axis='both',which='major',labelsize=15)
plt.show()

#%%
# PROB DENSITY SPECIALS
fig = plt.figure(figsize=(8,4))

Xvec=Vpsi_o[1] # Ocean gyres
Yvec=VdT_o[1]  # Ocean heating
Zvec=Vpsi_a[0] # Atmospheric zonal flow
T0=40000
Vector=Zvec[T0:]

density = gaussian_kde(Vector)
xs = np.linspace(np.min(Vector),np.max(Vector),500)
density.covariance_factor = lambda : 0.05
density._compute_covariance()
plt.plot(xs,density(xs),linewidth=3)
plt.xlabel(r'Value $y$',fontsize=15)
plt.ylabel(r'Probability density $p(y)$',fontsize=15)
plt.tick_params(axis='both',which='major',labelsize=15)
plt.show()