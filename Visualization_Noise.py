#Phase space

fig = plt.figure(figsize=(12,10))
fig.subplots_adjust(wspace = 0.2, hspace = 0.2)
ax1 = fig.add_subplot(2,2,1)
ax2 = fig.add_subplot(2,2,2)
ax3 = fig.add_subplot(2,2,3)
ax4 = fig.add_subplot(2,2,4)

ax1.plot(Vx[0],Vx[21],'k')
ax1.plot(X1,X22,'g',linewidth=2)
ax1.plot(Vpsi_a[0][80000:],Vpsi_o[1][80000:],'r')
ax1.set_xlabel('X1')
ax1.set_ylabel('X22')


ax2.plot(Vx[0],Vx[29],'k')
ax2.plot(X1,X30,'g',linewidth=2)
ax2.plot(Vpsi_a[0][80000:],VdT_o[1][80000:],'r')
ax2.set_xlabel('X1')
ax2.set_ylabel('X30')


ax3.plot(Vx[21],Vx[29],'k')
ax3.plot(X22,X30,'g',linewidth=2)
ax3.plot(Vpsi_o[1][80000:],VdT_o[1][80000:],'r')
ax3.set_xlabel('X22')
ax3.set_ylabel('X30')


ax4.plot(Vx[0],Vx[10],'k')
ax4.plot(X1,X11,'g',linewidth=2)
ax4.plot(Vpsi_a[0][80000:],Vtheta_a[0][80000:],'r')
ax4.set_xlabel('X1')
ax4.set_ylabel('X11')