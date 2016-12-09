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

toanalyzestart=50000

Fx1=np.abs(np.fft.fft(Psi_a(Xp1,Yp1,Vector)[toanalyzestart:]))**2.
Fx2=np.abs(np.fft.fft(Psi_o(Xp1,Yp1,Vector)[toanalyzestart:]))**2.
Fx3=np.abs(np.fft.fft(dT_a(Xp1,Yp1,Vector)[toanalyzestart:]))**2.
Fx4=np.abs(np.fft.fft(dT_o(Xp1,Yp1,Vector)[toanalyzestart:]))**2.

start=0
end=len(Fx1)/2
Freqvec=np.fft.fftfreq(len(times[toanalyzestart:]),d=10)
#end=np.int(len(times)/2)

fig, ((ax1,ax2),(ax3,ax4)) = plt.subplots(2,2,figsize=(10,6))

ax1.semilogy(Freqvec[start:end],Fx1[start:end],linewidth=2)
ax2.semilogy(Freqvec[start:end],Fx2[start:end],linewidth=2)
ax3.semilogy(Freqvec[start:end],Fx3[start:end],linewidth=2)
ax4.semilogy(Freqvec[start:end],Fx4[start:end],linewidth=2)

ax1.set_title(r'$\Psi_a$',fontsize=15)
ax2.set_title(r'$\Psi_o$',fontsize=15)
ax3.set_title(r'$\delta T_a$',fontsize=15)
ax4.set_title(r'$\delta T_o$',fontsize=15)

ax1.tick_params(axis='both',which='major',labelsize=10)
ax2.tick_params(axis='both',which='major',labelsize=10)
ax3.tick_params(axis='both',which='major',labelsize=10)
ax4.tick_params(axis='both',which='major',labelsize=10)

ax1.set_xlim([0,0.0005])
ax2.set_xlim([0,0.0005])
ax3.set_xlim([0,0.0005])
ax4.set_xlim([0,0.0005])

plt.show()

#%% PLOT EVOLUTION - SPEC components, AT SPECIFIED LOCATION
Nc=25
Vector=np.linspace(0,99999,100000).astype(np.int)

toanalyzestart=50000

Fx1=np.abs(np.fft.fft(Vpsi_a[0][toanalyzestart:]))**2.
Fx2=np.abs(np.fft.fft(Vpsi_o[1][toanalyzestart:]))**2.
Fx3=np.abs(np.fft.fft(Vtheta_a[0][toanalyzestart:]))**2.
Fx4=np.abs(np.fft.fft(VdT_o[1][toanalyzestart:]))**2.

start=1
end=len(Fx1)/2
Freqvec=np.fft.fftfreq(len(times[toanalyzestart:]),d=10)
#end=np.int(len(times)/2)

fig, ((ax1,ax2),(ax3,ax4)) = plt.subplots(2,2,figsize=(10,6))

ax1.semilogy(Freqvec[start:end],Fx1[start:end],linewidth=2)
ax2.semilogy(Freqvec[start:end],Fx2[start:end],linewidth=2)
ax3.semilogy(Freqvec[start:end],Fx3[start:end],linewidth=2)
ax4.semilogy(Freqvec[start:end],Fx4[start:end],linewidth=2)

ax1.set_title(r'$\Psi_a$(0)',fontsize=15)
ax2.set_title(r'$\Psi_o$(1)',fontsize=15)
ax3.set_title(r'$\theta$(0)',fontsize=15)
ax4.set_title(r'$\delta T_o$(1)',fontsize=15)

ax1.tick_params(axis='both',which='major',labelsize=10)
ax2.tick_params(axis='both',which='major',labelsize=10)
ax3.tick_params(axis='both',which='major',labelsize=10)
ax4.tick_params(axis='both',which='major',labelsize=10)

ax1.set_xlim([0,0.00025])
ax2.set_xlim([0,0.00025])
ax3.set_xlim([0,0.00025])
ax4.set_xlim([0,0.00025])

plt.show()


#%% PLOT EVOLUTION - All SPEC components
Nc=25
Vector=np.linspace(0,99999,100000).astype(np.int)

toanalyzestart=70000

F1x1=np.abs(np.fft.fft(V1_1[0][toanalyzestart:]))**2.
F1x2=np.abs(np.fft.fft(V1_2[1][toanalyzestart:]))**2.
F1x3=np.abs(np.fft.fft(V1_3[0][toanalyzestart:]))**2.
F1x4=np.abs(np.fft.fft(V1_4[1][toanalyzestart:]))**2.

F2x1=np.abs(np.fft.fft(V2_1[0][toanalyzestart:]))**2.
F2x2=np.abs(np.fft.fft(V2_2[1][toanalyzestart:]))**2.
F2x3=np.abs(np.fft.fft(V2_3[0][toanalyzestart:]))**2.
F2x4=np.abs(np.fft.fft(V2_4[1][toanalyzestart:]))**2.

F3x1=np.abs(np.fft.fft(V3_1[0][toanalyzestart:]))**2.
F3x2=np.abs(np.fft.fft(V3_2[1][toanalyzestart:]))**2.
F3x3=np.abs(np.fft.fft(V3_3[0][toanalyzestart:]))**2.
F3x4=np.abs(np.fft.fft(V3_4[1][toanalyzestart:]))**2.

F4x1=np.abs(np.fft.fft(V4_1[0][toanalyzestart:]))**2.
F4x2=np.abs(np.fft.fft(V4_2[1][toanalyzestart:]))**2.
F4x3=np.abs(np.fft.fft(V4_3[0][toanalyzestart:]))**2.
F4x4=np.abs(np.fft.fft(V4_4[1][toanalyzestart:]))**2.

F5x1=np.abs(np.fft.fft(V5_1[0][toanalyzestart:]))**2.
F5x2=np.abs(np.fft.fft(V5_2[1][toanalyzestart:]))**2.
F5x3=np.abs(np.fft.fft(V5_3[0][toanalyzestart:]))**2.
F5x4=np.abs(np.fft.fft(V5_4[1][toanalyzestart:]))**2.

start=1
end=len(Fx1)/2
Freqvec=np.fft.fftfreq(len(times[toanalyzestart:]),d=10)
#end=np.int(len(times)/2)

fig, ((ax1,ax2),(ax3,ax4)) = plt.subplots(2,2,figsize=(10,6))

ax1.semilogy(1/Freqvec[start:end]/f0/3600/24/365,F1x1[start:end],linewidth=2)
ax1.semilogy(1/Freqvec[start:end]/f0/3600/24/365,F2x1[start:end],linewidth=2)
ax1.semilogy(1/Freqvec[start:end]/f0/3600/24/365,F3x1[start:end],linewidth=2)
ax1.semilogy(1./Freqvec[start:end]/f0/3600/24/365,F4x1[start:end],linewidth=2)
ax1.semilogy(1/Freqvec[start:end]/f0/3600/24/365,F5x1[start:end],linewidth=2)

ax2.semilogy(1/Freqvec[start:end]/f0/3600/24/365,F1x2[start:end],linewidth=2)
ax2.semilogy(1/Freqvec[start:end]/f0/3600/24/365,F2x2[start:end],linewidth=2)
ax2.semilogy(1/Freqvec[start:end]/f0/3600/24/365,F3x2[start:end],linewidth=2)
ax2.semilogy(1/Freqvec[start:end]/f0/3600/24/365,F4x2[start:end],linewidth=2)
ax2.semilogy(1/Freqvec[start:end]/f0/3600/24/365,F5x2[start:end],linewidth=2)

ax3.semilogy(1/Freqvec[start:end]/f0/3600/24/365,F1x3[start:end],linewidth=2)
ax3.semilogy(1/Freqvec[start:end]/f0/3600/24/365,F2x3[start:end],linewidth=2)
ax3.semilogy(1/Freqvec[start:end]/f0/3600/24/365,F3x3[start:end],linewidth=2)
ax3.semilogy(1/Freqvec[start:end]/f0/3600/24/365,F4x3[start:end],linewidth=2)
ax3.semilogy(1/Freqvec[start:end]/f0/3600/24/365,F5x3[start:end],linewidth=2)

ax4.semilogy(1/Freqvec[start:end]/f0/3600/24/365,F1x4[start:end],linewidth=2)
ax4.semilogy(1/Freqvec[start:end]/f0/3600/24/365,F2x4[start:end],linewidth=2)
ax4.semilogy(1/Freqvec[start:end]/f0/3600/24/365,F3x4[start:end],linewidth=2)
ax4.semilogy(1/Freqvec[start:end]/f0/3600/24/365,F4x4[start:end],linewidth=2)
ax4.semilogy(1/Freqvec[start:end]/f0/3600/24/365,F5x4[start:end],linewidth=2)

ax1.set_title(r'$\Psi_a$(0)',fontsize=15)
ax2.set_title(r'$\Psi_o$(1)',fontsize=15)
ax3.set_title(r'$\theta$(0)',fontsize=15)
ax4.set_title(r'$\delta T_o$(1)',fontsize=15)

#ax1.tick_params(axis='both',which='major',labelsize=10)
#ax2.tick_params(axis='both',which='major',labelsize=10)
#ax3.tick_params(axis='both',which='major',labelsize=10)
#ax4.tick_params(axis='both',which='major',labelsize=10)

ax1.set_xlim([0,60])
ax2.set_xlim([0,60])
ax3.set_xlim([0,60])
ax4.set_xlim([0,60])

ax1.legend(['1e-9','5e-9','1e-8','5e-8','1e-7'])

plt.show()