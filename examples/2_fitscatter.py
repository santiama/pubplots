import matplotlib.pyplot as plt
from pubplots import PlotData
import pubplots.plot as pbt

fit1 = PlotData()
# Use the walk and find method to find the fit data
fit1.walkandfind(startpath='data', search='fit',
                 labels=['x=0', '0.1', '0.2', '0.3'], header=None)

# fit scatered data with np.polyfit, deg is by default 1, prints fit paramaters and errors
fit1.fit(deg=1)

# Here we use the individual commands rather than the quick plot method
fig = plt.figure(figsize=(8, 6), facecolor='white')
ax = plt.subplot(111)
pbt.modern_style(ax)
pbt.axis_labels(ax, '10$^{3}$/RT', 'ln(k)')
pbt.plot_scatter(ax, fit1.yset, fillstyle='none', markeredgewidth=2.0)
pbt.plot_lines(ax, fit1.fits)
pbt.label_lines(ax, fit1.fits, labels=fit1.labels, at_x=[0.18, 0.17, 0.157, 0.133])
ax.set_xlim(0.125, 0.35)
pbt.save('2_fitscatter')
plt.show()
