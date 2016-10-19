import matplotlib.pyplot as plt
from pubplots import PlotData
import pubplots.plot as pbt

kin = PlotData()
# Use the walk and find method to find the fit data
kin.walkandfind(startpath='data', search='kin', xcol=0, ycols=[1],
                labels=['200 $^\circ$C', '250', '300', '350', '400', '500'],
                xaxislabel='Time [min]', yaxislabel='Fraction complete', sep=' ')


fig = plt.figure(figsize=(8, 6), facecolor='white')
ax = plt.subplot()
pbt.quick_semimodern(ax, kin, at_x=[2.3, 1.5, 1.5, 0.7, 0.5, 0.58])
ax.set_xlim(0, 2.2)
ax.set_ylim(0, 1.05)

# Remove the two fastest reactions for the inset plot
kin.yset.pop()
kin.yset.pop()
axin = pbt.inset_plot(fig, ax, kin.yset, xlabel='Time [min]', ylabel='Fraction complete',
                      label=True, at_x=[30, 15, 15, 15], labels=kin.labels, style='semimodern')
axin.set_xlim(0, 40)
axin.set_ylim(0, 1.05)
pbt.save('4_inset_kinetics')
# In this case plt.show() does not display correctly. But the saved image does.
plt.show()
