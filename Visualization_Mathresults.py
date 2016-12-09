X = PC['EQ1'].getSpecialPoint('B1')
X.labels['B']['data'].X

PC['EQ1'].display(axes=(1,2,1))
plt.xscale('log')
PC['EQ1'].display(('dp','X22'),axes=(1,2,2))
plt.xscale('log')
PC.plot.info()
