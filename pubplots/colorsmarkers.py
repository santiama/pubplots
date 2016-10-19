"""The colors and markers used in pubplots.plot

Attributes
----------
BLACK : list of black color tuples
    [(0.05, 0.05, 0.05)]*20
CB10 : list of color tupples
    color blind 10 from
    http://tableaufriction.blogspot.de/2012/11/finally-you-can-use-tableau-data-colors.html
TB10 : list of color tuples
    tableau 20 colors from
    http://tableaufriction.blogspot.de/2012/11/finally-you-can-use-tableau-data-colors.html
TB20 : list of color tuples
    tableau 20 colors from
    http://tableaufriction.blogspot.de/2012/11/finally-you-can-use-tableau-data-colors.html
TB5 : list of color tuples
    tableau 5
GREY : list of grey tuple colors
    [(0.34, 0.34, 0.39)]*20
PBMK : list of markers
    ['o', 's', 'v', 'p', '^', '8', '*', '>', '<', 'x', '+']
pubdashes : list of dash seperations
pubcolors : dictionary of strings to colors
    pubcolors={'tb10':TB10, 'tb20': TB20, 'tb5':TB5, 'cb10':CB10, 'black':BLACK, 'grey':GREY}
publs : dictionary of linestyles
pubmarkers : dictionary of marker lists
    pubmarkers={'var':PBMK,'o':20*['o'], 's':20*['s'], 'v': 20*['v']}
"""


# Tableau 20 clors
TB20 = [(31, 119, 180), (174, 199, 232), (255, 127, 14), (255, 187, 120),
        (44, 160, 44), (152, 223, 138), (214, 39, 40), (255, 152, 150),
        (148, 103, 189), (197, 176, 213), (140, 86, 75), (196, 156, 148),
        (227, 119, 194), (247, 182, 210), (127, 127, 127), (199, 199, 199),
        (188, 189, 34), (219, 219, 141), (23, 190, 207), (158, 218, 229)]
# Tableau 10 colors
TB10 = [(31, 119, 180), (255, 127, 14), (44, 160, 44), (214, 39, 40),
        (148, 103, 189), (140, 86, 75), (227, 119, 194), (127, 127, 127),
        (188, 189, 34), (23, 190, 207)]

TB5 = [(31, 119, 180), (214, 39, 40), (255, 127, 14), (44, 160, 44),
       (148, 103, 189)]

# All Black
BLACK = [(0.05, 0.05, 0.05)]*20

# Grey
GREY = [(0.34, 0.34, 0.39)]*20

# Color Blind 10
CB10 = [(0, 107, 164), (255, 128, 14), (171, 171, 171), (89, 89, 89), (95, 158, 209),
        (200, 82, 0), (137, 137, 137), (162, 200, 236), (255, 188, 121), (207, 207, 207)]

PBMK = ['o', 's', 'v', 'p', '^', '8', '*', '>', '<', 'x', '+']

# Scale the RGB values to the [0, 1] range, which is the format matplotlib accepts.
for i in range(len(TB20)):
    r, g, b = TB20[i]
    TB20[i] = (r / 255., g / 255., b / 255.)
# Scale the RGB values to the [0, 1] range, which is the format matplotlib accepts.
for i in range(len(TB10)):
    r, g, b = TB10[i]
    TB10[i] = (r / 255., g / 255., b / 255.)
    r, g, b = CB10[i]
    CB10[i] = (r / 255., g / 255., b / 255.)

for i in range(len(TB5)):
    r, g, b = TB5[i]
    TB5[i] = (r / 255., g / 255., b / 255.)

pubcolors={'tb10':TB10, 'tb20': TB20, 'tb5':TB5, 'cb10':CB10, 'black':BLACK, 'grey':GREY}
pubmarkers={'var':PBMK,'o':20*['o'], 's':20*['s'], 'v': 20*['v']}
publs={'-':20*['-'], '--':20*['--']}
pubdashes = [[18,4], [14,4,8,4], [18,14], [20,4,6,4], [28,8], [18,4,12,4], [10,6], [16,4,14,6]]
for i, entry in enumerate(pubdashes):
    pubdashes[i]=[2*num for num in entry]
