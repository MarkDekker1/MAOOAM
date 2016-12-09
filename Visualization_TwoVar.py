# --------------------------------------------------------------------------- #
# Check out two variables and their phase space
# --------------------------------------------------------------------------- #

start=100
end=len(t)-1
each=1
fig = plt.figure(figsize=(12,6))
fig.subplots_adjust(wspace = 0.2, hspace = 0.4)
ax1 = fig.add_subplot(2,2,1)
ax2 = fig.add_subplot(2,2,2)
ax3 = fig.add_subplot(2,2,3)
ax1.plot(t[start:end:each],X1[start:end:each], 'b-')
ax2.plot(t[start:end:each],X22[start:end:each], 'r-')
ax3.plot(X1[start:end:each], X22[start:end:each], 'k')

ax1.set_title("X1")
ax1.set_xlabel("time")
ax1.grid()
ax2.set_title("X22")
ax2.set_xlabel("time")
ax2.grid()
#ax1.set_yscale('log')

ax3.set_xlabel("X1")
ax3.set_ylabel('X22')  
ax3.set_title("Phase space")
#ax3.set_xscale('log')
ax3.grid()