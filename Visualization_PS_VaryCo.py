# --------------------------------------------------------------------------- #
# VARY Co
# --------------------------------------------------------------------------- #

lda=20
d=1e-8

X1,X2,X3,X4,X5,X6,X7,X8,X9,X10=V1_1
X11,X12,X13,X14,X15,X16,X17,X18,X19,X20=V1_3
X21,X22,X23,X24,X25,X26,X27,X28=V1_2
X29,X30,X31,X32,X33,X34,X35,X36=V1_4
t = times
co=100

x1,x2,x3,x4,x5,x6,x7,x8,x9,x10,x11,x12,x13,x14,x15,x16,x17,x18,x19,x20,x21,x22,x23,x24,x25,x26,x27,x28,x29,x30,x31,x32,x33,x34,x35,x36 = sm.symbols('X1,X2,X3,X4,X5,X6,X7,X8,X9,X10,X11,X12,X13,X14,X15,X16,X17,X18,X19,X20,X21,X22,X23,X24,X25,X26,X27,X28,X29,X30,X31,X32,X33,X34,X35,X36')

listeqns=[]
for i in range(0,36):
    listeqns.append(eval(EQNS[AllVars[i]].lower()))
    
# --------------------------------------------------------------------------- #
# Create subplots and phase space tendencies
# --------------------------------------------------------------------------- #
from matplotlib.pyplot import cm
    
AmountArrows=25
mappy=cm.coolwarm
linewidthy=1
dotcolor='b'
factor=1
    
fig = plt.figure(figsize=(12,5))
fig.subplots_adjust(wspace = 0.2, hspace = 0.2)
ax1 = fig.add_subplot(1,3,1)
ax2 = fig.add_subplot(1,3,2)
ax3 = fig.add_subplot(1,3,3)

# define dimensions for grid (std)
dimx1=np.linspace(0.02,0.05,AmountArrows)
dimx22=np.linspace(-0.0012,0.0012,AmountArrows)
dimx30=np.linspace(-0.1,0.40,AmountArrows)
dimx11=np.linspace(0.025,0.042,AmountArrows)


# define dimensions for grid (d1e-7)
#dimx1=np.linspace(0.035,0.045,AmountArrows)
#dimx22=np.linspace(0.0005,0.0015,AmountArrows)
#dimx30=np.linspace(-0.10,0.60,AmountArrows)
#dimx11=np.linspace(0.025,0.042,AmountArrows)

tchoose=9559#t[len(t)-1]
y1=X1[tchoose]
y2=X2[tchoose]
y3=X3[tchoose]
y4=X4[tchoose]
y5=X5[tchoose]
y6=X6[tchoose]
y7=X7[tchoose]
y8=X8[tchoose]
y9=X9[tchoose]
y10=X10[tchoose]
y11=X11[tchoose]
y12=X12[tchoose]
y13=X13[tchoose]
y14=X14[tchoose]
y15=X15[tchoose]
y16=X16[tchoose]
y17=X17[tchoose]
y18=X18[tchoose]
y19=X19[tchoose]
y20=X20[tchoose]
y21=X21[tchoose]
y22=X22[tchoose]
y23=X23[tchoose]
y24=X24[tchoose]
y25=X25[tchoose]
y26=X26[tchoose]
y27=X27[tchoose]
y28=X28[tchoose]
y29=X29[tchoose]
y30=X30[tchoose]
y31=X31[tchoose]
y32=X32[tchoose]
y33=X33[tchoose]
y34=X34[tchoose]
y35=X35[tchoose]
y36=X36[tchoose]


# PLOT 1
Y1 , Y22  = np.meshgrid(dimx1,dimx22)
DX1,DX2,DX3,DX4,DX5,DX6,DX7,DX8,DX9,DX10,DX11,DX12,DX13,DX14,DX15,DX16,DX17,DX18,DX19,DX20,DX21,DX22,DX23,DX24,DX25,DX26,DX27,DX28,DX29,DX30,DX31,DX32,DX33,DX34,DX35,DX36 = Equations([Y1,y2,y3,y4,y5,y6,y7,y8,y9,y10,y11,y12,y13,y14,y15,y16,y17,y18,y19,y20,y21,Y22,y23,y24,y25,y26,y27,y28,y29,y30,y31,y32,y33,y34,y35,y36])
DX22=factor*DX22
M = (np.hypot(DX1, DX22))
M[M == 0] = 1.
ax1.streamplot(Y1, Y22, DX1, DX22, color=M,cmap=mappy,linewidth=2)
ax1.scatter([X1[tchoose]],[X22[tchoose]],s=200,c=dotcolor,zorder=10)
ax1.set_xlabel("X1")
ax1.set_ylabel("X22")
ax1.plot(X1, X22, 'k-',linewidth=linewidthy)
ax1.grid()
ax1.legend(loc='best')
ax1.legend(loc='best')
ax1.set_xlim([np.min(dimx1),np.max(dimx1)])
ax1.set_ylim([np.min(dimx22),np.max(dimx22)])


X1,X2,X3,X4,X5,X6,X7,X8,X9,X10=V2_1
X11,X12,X13,X14,X15,X16,X17,X18,X19,X20=V2_3
X21,X22,X23,X24,X25,X26,X27,X28=V2_2
X29,X30,X31,X32,X33,X34,X35,X36=V2_4
t = times
co=200

x1,x2,x3,x4,x5,x6,x7,x8,x9,x10,x11,x12,x13,x14,x15,x16,x17,x18,x19,x20,x21,x22,x23,x24,x25,x26,x27,x28,x29,x30,x31,x32,x33,x34,x35,x36 = sm.symbols('X1,X2,X3,X4,X5,X6,X7,X8,X9,X10,X11,X12,X13,X14,X15,X16,X17,X18,X19,X20,X21,X22,X23,X24,X25,X26,X27,X28,X29,X30,X31,X32,X33,X34,X35,X36')

listeqns=[]
for i in range(0,36):
    listeqns.append(eval(EQNS[AllVars[i]].lower()))

tchoose=9559#t[len(t)-1]
y1=X1[tchoose]
y2=X2[tchoose]
y3=X3[tchoose]
y4=X4[tchoose]
y5=X5[tchoose]
y6=X6[tchoose]
y7=X7[tchoose]
y8=X8[tchoose]
y9=X9[tchoose]
y10=X10[tchoose]
y11=X11[tchoose]
y12=X12[tchoose]
y13=X13[tchoose]
y14=X14[tchoose]
y15=X15[tchoose]
y16=X16[tchoose]
y17=X17[tchoose]
y18=X18[tchoose]
y19=X19[tchoose]
y20=X20[tchoose]
y21=X21[tchoose]
y22=X22[tchoose]
y23=X23[tchoose]
y24=X24[tchoose]
y25=X25[tchoose]
y26=X26[tchoose]
y27=X27[tchoose]
y28=X28[tchoose]
y29=X29[tchoose]
y30=X30[tchoose]
y31=X31[tchoose]
y32=X32[tchoose]
y33=X33[tchoose]
y34=X34[tchoose]
y35=X35[tchoose]
y36=X36[tchoose]

# PLOT 2
Y1 , Y22  = np.meshgrid(dimx1,dimx22)
DX1,DX2,DX3,DX4,DX5,DX6,DX7,DX8,DX9,DX10,DX11,DX12,DX13,DX14,DX15,DX16,DX17,DX18,DX19,DX20,DX21,DX22,DX23,DX24,DX25,DX26,DX27,DX28,DX29,DX30,DX31,DX32,DX33,DX34,DX35,DX36 = Equations([Y1,y2,y3,y4,y5,y6,y7,y8,y9,y10,y11,y12,y13,y14,y15,y16,y17,y18,y19,y20,y21,Y22,y23,y24,y25,y26,y27,y28,y29,y30,y31,y32,y33,y34,y35,y36])
DX22=factor*DX22
M = (np.hypot(DX1, DX22))
M[M == 0] = 1.
ax2.streamplot(Y1, Y22, DX1, DX22, color=M,cmap=mappy,linewidth=2)
ax2.scatter([X1[tchoose]],[X22[tchoose]],s=200,c=dotcolor,zorder=10)
ax2.set_xlabel("X1")
ax2.set_ylabel("X22")
ax2.plot(X1, X22, 'k-',linewidth=linewidthy)
ax2.grid()
ax2.legend(loc='best')
ax2.legend(loc='best')
ax2.set_xlim([np.min(dimx1),np.max(dimx1)])
ax2.set_ylim([np.min(dimx22),np.max(dimx22)])


X1,X2,X3,X4,X5,X6,X7,X8,X9,X10=V3_1
X11,X12,X13,X14,X15,X16,X17,X18,X19,X20=V3_3
X21,X22,X23,X24,X25,X26,X27,X28=V3_2
X29,X30,X31,X32,X33,X34,X35,X36=V3_4
t = times
co=350

x1,x2,x3,x4,x5,x6,x7,x8,x9,x10,x11,x12,x13,x14,x15,x16,x17,x18,x19,x20,x21,x22,x23,x24,x25,x26,x27,x28,x29,x30,x31,x32,x33,x34,x35,x36 = sm.symbols('X1,X2,X3,X4,X5,X6,X7,X8,X9,X10,X11,X12,X13,X14,X15,X16,X17,X18,X19,X20,X21,X22,X23,X24,X25,X26,X27,X28,X29,X30,X31,X32,X33,X34,X35,X36')

listeqns=[]
for i in range(0,36):
    listeqns.append(eval(EQNS[AllVars[i]].lower()))

tchoose=9559#t[len(t)-1]
y1=X1[tchoose]
y2=X2[tchoose]
y3=X3[tchoose]
y4=X4[tchoose]
y5=X5[tchoose]
y6=X6[tchoose]
y7=X7[tchoose]
y8=X8[tchoose]
y9=X9[tchoose]
y10=X10[tchoose]
y11=X11[tchoose]
y12=X12[tchoose]
y13=X13[tchoose]
y14=X14[tchoose]
y15=X15[tchoose]
y16=X16[tchoose]
y17=X17[tchoose]
y18=X18[tchoose]
y19=X19[tchoose]
y20=X20[tchoose]
y21=X21[tchoose]
y22=X22[tchoose]
y23=X23[tchoose]
y24=X24[tchoose]
y25=X25[tchoose]
y26=X26[tchoose]
y27=X27[tchoose]
y28=X28[tchoose]
y29=X29[tchoose]
y30=X30[tchoose]
y31=X31[tchoose]
y32=X32[tchoose]
y33=X33[tchoose]
y34=X34[tchoose]
y35=X35[tchoose]
y36=X36[tchoose]


# PLOT 3
Y1 , Y22  = np.meshgrid(dimx1,dimx22)
DX1,DX2,DX3,DX4,DX5,DX6,DX7,DX8,DX9,DX10,DX11,DX12,DX13,DX14,DX15,DX16,DX17,DX18,DX19,DX20,DX21,DX22,DX23,DX24,DX25,DX26,DX27,DX28,DX29,DX30,DX31,DX32,DX33,DX34,DX35,DX36 = Equations([Y1,y2,y3,y4,y5,y6,y7,y8,y9,y10,y11,y12,y13,y14,y15,y16,y17,y18,y19,y20,y21,Y22,y23,y24,y25,y26,y27,y28,y29,y30,y31,y32,y33,y34,y35,y36])
DX22=factor*DX22
M = (np.hypot(DX1, DX22))
M[M == 0] = 1.
ax3.streamplot(Y1, Y22, DX1, DX22, color=M,cmap=mappy,linewidth=2)
ax3.scatter([X1[tchoose]],[X22[tchoose]],s=200,c=dotcolor,zorder=10)
ax3.set_xlabel("X1")
ax3.set_ylabel("X22")
ax3.plot(X1, X22, 'k-',linewidth=linewidthy)
ax3.grid()
ax3.legend(loc='best')
ax3.legend(loc='best')
ax3.set_xlim([np.min(dimx1),np.max(dimx1)])
ax3.set_ylim([np.min(dimx22),np.max(dimx22)])
