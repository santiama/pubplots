import matplotlib.pyplot as plt
from pubplots import PlotData
import pubplots.plot as pbt

# A plot of some reaction rate data of mine for the re-oxidation of Ce1-xZrxO(2-d)
# These files are delimted by tabs so that needs to be specified using sep='\t'

# Load kinetic data
pco = PlotData()
pco.walkandfind(startpath='data', search='PC_', xaxislabel='Time [s]',
                yaxislabel='Fraction complete', yraxislabel='Temperature [$^\\circ$C]',
                labels=['x = 0', '0.05', '0.1', '0.2', '0.3 '], header=None, sep='\t')

# Load temperature data for the right hand axis
rlabel = 'T$_{\mathrm{max}}$ $ \\approx$ 860 $^{\circ}$C $\\rightarrow$'
pco.onefile('data/t_T_ox.txt', ycols=[], yrcols=[1],
            yrlabels=[rlabel], header=None, sep='\t')

# In this case the pbt.quick_modern() method sees that there is only one data set for the
# right axes and colors it grey, and then uses colors for the left axes
fig = plt.figure(figsize=(8.5, 6), facecolor='white')
ax = plt.subplot(111)
axr = pbt.quick_modern(ax, pco, at_x=[60, 90, 120, 140, 160], scatter=True)
ax.set_xlim(0, 240)
ax.set_ylim(0, 1)
pbt.save('7_scatter')
plt.tight_layout()
plt.show()
