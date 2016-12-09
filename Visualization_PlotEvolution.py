# PLOT EVOLUTION - FULL COMPONENTS, AT SPECIFIED LOCATION
Xp1=3.2
Yp1=2.5
Xp2=1
Yp2=2.5
Xp3=3.2
Yp3=0.75
Xp4=1
Yp4=0.75
Nc=25
Vector=np.linspace(0,99999,100000).astype(np.int)

fig, ((ax1,ax2),(ax3,ax4)) = plt.subplots(2,2,figsize=(10,6))

ax1.plot(time,Psi_a(Xp1,Yp1,Vector),linewidth=2)
ax2.plot(time,Psi_o(Xp1,Yp1,Vector),linewidth=2)
ax3.plot(time,dT_a(Xp1,Yp1,Vector),linewidth=2)
ax4.plot(time,dT_o(Xp1,Yp1,Vector),linewidth=2)

ax1.plot(time,Psi_a(Xp2,Yp2,Vector),linewidth=2)
ax2.plot(time,Psi_o(Xp2,Yp2,Vector),linewidth=2)
ax3.plot(time,dT_a(Xp2,Yp2,Vector),linewidth=2)
ax4.plot(time,dT_o(Xp2,Yp2,Vector),linewidth=2)

ax1.plot(time,Psi_a(Xp3,Yp3,Vector),linewidth=2)
ax2.plot(time,Psi_o(Xp3,Yp3,Vector),linewidth=2)
ax3.plot(time,dT_a(Xp3,Yp3,Vector),linewidth=2)
ax4.plot(time,dT_o(Xp3,Yp3,Vector),linewidth=2)

ax1.plot(time,Psi_a(Xp4,Yp4,Vector),linewidth=2)
ax2.plot(time,Psi_o(Xp4,Yp4,Vector),linewidth=2)
ax3.plot(time,dT_a(Xp4,Yp4,Vector),linewidth=2)
ax4.plot(time,dT_o(Xp4,Yp4,Vector),linewidth=2)

ax1.set_title(r'$\Psi_a$',fontsize=15)
ax2.set_title(r'$\Psi_o$',fontsize=15)
ax3.set_title(r'$\delta T_a$',fontsize=15)
ax4.set_title(r'$\delta T_o$',fontsize=15)

ax1.tick_params(axis='both',which='major',labelsize=10)
ax2.tick_params(axis='both',which='major',labelsize=10)
ax3.tick_params(axis='both',which='major',labelsize=10)
ax4.tick_params(axis='both',which='major',labelsize=10)

plt.show()

#%%
# PLOT EVOLUTION - SINGLE COMP
Nc=25
Vector=np.linspace(0,99999,100000).astype(np.int)

fig = plt.figure(figsize=(10,6))
#plt.plot(time,Lock_d10[0],'m',linewidth=2,label='1e-10')
#plt.plot(time,Lock_lowd[0],'k',linewidth=2,label='1e-9')
#plt.plot(time,Lock_d5_9[0],'--k',linewidth=2,label='5e-9')
plt.plot(time,Vpsi[0],'b',linewidth=2,label='1e-8')
#plt.plot(time,Lock_d5_8[0],'--',linewidth=2,label='5e-8')
#plt.plot(time,Lock_highd[0],'r',linewidth=2,label='1e-7')
#plt.plot(time,Lock_d6[0],'g',linewidth=2,label='1e-6')
#plt.plot(time,Lock_d5[0],'y',linewidth=2,label='1e-5')
plt.title(r'$\Psi_a$',fontsize=15)
plt.tick_params(axis='both',which='major',labelsize=10)
#plt.ylim([0.025,0.045])
plt.legend(loc='best')
plt.show()