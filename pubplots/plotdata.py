"""Contains the PlotData class for preparing plot data from pandas dataframes and csv files
"""
import numpy as np
import pandas as pd
import math
import os


# This function is needed as the default function for a method in Data()

class PlotData(object):

    """used to store information from csv files for plotting. It can smartly set the axes labels
    and line labels using the file headers

    Attributes
    ----------
    files : list of loaded files
    fits : list of fits of the plot data
    frames : list of pandas DataFrames that the data is taken from
    xaxislabel : label to be put on the xaxis
    yaxislabel : label to be put on the yaxis
    yset : list of data to be plotted [[x array,y array], [x2 array, y2 array].....]
    labels : list of labels for the yset
    yerrors : list of yerror arrays to go with yset
    yrset : list of data to be plotted to right hand axes [[x array,y array], [x2 array, y2 array].....]
    yraxislabel : right hand axes label
    yrlabels : list of labels for the right hand axes data
    yr2set : list of data to be plotted to right hand axes [[x array,y array], [x2 array, y2 array].....]
    yr2axislabel : second right hand axes label
    yr2labels : second right hand line labels
    """

    def __init__(self):
        self.files = []
        self.frames = []
        self.yset = []
        self.yrset = []
        self.yr2set = []
        self.yerrors = []
        self.xerrors = []
        self.fits = []
        self.labels = []
        self.yrlabels = []
        self.yr2labels = []
        self.xaxislabel = None
        self.yaxislabel = None
        self.yraxislabel = None
        self.yr2axislabel = None

    def prepare_frame(self, dataframe, xcol=0,
            ycols=[1], labels=[],
            yrcols=[], yrlabels=[],
            yr2cols=[], yr2labels=[],
            xerrors=[], yerrors=[],
            xaxislabel=None, yaxislabel=None, yraxislabel=None, yr2axislabel=None):
        """Specifiy what data is what in the pandas data. This essentially builds list of
        pointers to access the correct data for plotting

        Parameters
        ----------
        dataframe : pandas.DataFrame object to set the plotting data from
        xcol : int, optional
            position of the xdata collumn
        ycols : list of integers, optional
            list of collumns to use for ydata
        labels : list, optional
            list of labels for the ycols data
        yrcols : list, optional
            list of collumns to be plotted to a right hand axes
        yrlabels : list, optional
            list of labels to go with the right hand axes data
        yr2cols : list of integers, optional
            list of columns to be plot to second right hand axes
        yr2labels : list, optional
            labels to go with second right hand axes
        xerrors : list of integers, optional
        yerrors : list of integers, optional
            list of collumns to use as the yerrors for the yset data
        xaxislabel : str, optional
        yaxislabel : str, optional
        yraxislabel : str, optional
        yr2axislabel : str, optional
            Description
        """
        self.frames.append(dataframe)
        # make pointers to the data in the yset, yrset lists
        for ycol in ycols:
            self.yset.append([self.frames[-1].iloc[:, xcol], self.frames[-1].iloc[:, ycol]])
        for ycol in yrcols:
            self.yrset.append([self.frames[-1].iloc[:, xcol], self.frames[-1].iloc[:, ycol]])
        for ycol in yr2cols:
            self.yr2set.append([self.frames[-1].iloc[:, xcol], self.frames[-1].iloc[:, ycol]])
        for ercol in yerrors:
            self.yerrors.append([self.frames[-1].iloc[:, xcol], self.frames[-1].iloc[:, ercol]])
        for ercol in xerrors:
            self.xrerrors.append([self.frames[-1].iloc[:, xcol], self.frames[-1].iloc[:, ercol]])
        # Set axis labels
        if xaxislabel:
            self.xaxislabel = xaxislabel
        elif self.xaxislabel is None and self.yset!=[]:
            self.xaxislabel = self.yset[0][0].name
        if yaxislabel:
            self.yaxislabel = yaxislabel
        elif self.yaxislabel is None and self.yset!=[]:
            self.yaxislabel = self.yset[0][1].name
        if yraxislabel:
            self.yraxislabel = yraxislabel
        elif self.yraxislabel is None and self.yrset!=[]:
            self.yraxislabel = self.yrset[0][1].name
        if yr2axislabel:
            self.yr2axislabel = yr2axislabel
        elif self.yr2axislabel is None and self.yr2set!=[]:
            self.yr2axislabel = self.yr2set[0][1].name
        # If no labels are given, take them from the pandas DataFrame labels
        if labels != []:
            self.labels+=labels
        else:
            for ycol in ycols:
                self.labels.append(self.frames[-1].iloc[:, ycol].name)
        if yrlabels != []:
            self.yrlabels+=yrlabels
        else:
            for ycol in yrcols:
                self.yrlabels.append(self.frames[-1].iloc[:, ycol].name)
        if yr2labels != []:
            self.yr2labels+=yr2labels
        else:
            for ycol in yr2cols:
                self.yr2labels.append(self.frames[-1].iloc[:, ycol].name)

    def onefile(self, filename, header=0, xcol=0,
            ycols=[1], labels=[],
            yrcols=[], yrlabels=[],
            yr2cols=[], yr2labels=[],
            xerrors=[], yerrors=[], yrerrors=[], yr2errors=[],
            xaxislabel=None, yaxislabel=None, yraxislabel=None, yr2axislabel=None,
            **kwargs):
        """Add data from a single file to our data set, pass **kwargs to pandas.read_csv and then
        uses prepare frame

        Parameters
        ----------
        filename : str
            The file to be processed
        header : int, optional
            Which row to use as a header, default is header=0 which takes the first row
        other paramaters:
            see PlotData.prepare_frame method
        **kwargs : TYPE
            aditional arguements passed to pandas.read_csv method
        """
        self.files.append(filename)
        self.prepare_frame(pd.read_csv(filename, header=header, **kwargs), xcol=xcol,
                           ycols=ycols, labels=labels, yrcols=yrcols, yrlabels=yrlabels,
                           yr2cols=yr2cols, yr2labels=yr2labels, xerrors=xerrors, yerrors=yerrors,
                           xaxislabel=xaxislabel, yaxislabel=yaxislabel,
                           yraxislabel=yraxislabel, yr2axislabel=yr2axislabel)

    def filelist(self, files=[], header=0, xcol=0,
            ycols=[1], labels=[],
            yrcols=[], yrlabels=[],
            yr2cols=[], yr2labels=[],
            xerrors=[], yerrors=[], yrerrors=[], yr2errors=[],
            xaxislabel=None, yaxislabel=None, yraxislabel=None, yr2axislabel=None,
            **kwargs):
        """Load a list of files, pass **kwargs to pandas.read_csv

        Parameters
        ----------
        files : list of strings, optional
            list of files to be loaded
        header : int, optional
            Which row to use as a header, default is header=0 which takes the first row
        other paramaters:
            see PlotData.prepare_frame method
        **kwargs : TYPE
            aditional arguements passed to pandas.read_csv method
        """
        for filename in files:
            self.files.append(filename)
            self.prepare_frame(pd.read_csv(filename, header=header, **kwargs), xcol=xcol,
                               ycols=ycols, labels=labels, yrcols=yrcols, yrlabels=yrlabels,
                               yr2cols=yr2cols, yr2labels=yr2labels, xerrors=xerrors,
                               yerrors=yerrors,
                               xaxislabel=xaxislabel, yaxislabel=yaxislabel,
                               yraxislabel=yraxislabel, yr2axislabel=yr2axislabel)

    def walkandfind(self, startpath='data', search=None, header=0, xcol=0,
            ycols=[1], labels=[],
            yrcols=[], yrlabels=[],
            yr2cols=[], yr2labels=[],
            xerrors=[], yerrors=[],
            xaxislabel=None, yaxislabel=None, yraxislabel=None, yr2axislabel=None,
            **kwargs):
        """Search in a specified path for files containing a certain string and then load them
        up as data.The path can be relative or an absolute path.

        Parameters
        ----------
        startpath : str, optional
            Description
        search : str, optional
            load file names containing this string, default is '.csv'.
        header : int, optional
            Which row to use as a header, default is header=0 which takes the first row
        other paramaters:
            see PlotData.prepare_frame method
        **kwargs : TYPE
            aditional arguements passed to pandas.read_csv method
        """
        for root, dirs, files in os.walk(startpath):
            load = []
            # make list of files matching the search
            for filename in files:
                if search is None:
                    load.append(filename)
                elif filename.find(search) != -1:
                    load.append(filename)
            load.sort()
            self.files+=load
            print('Files Loaded:')
            for filename in load:
                print(filename)
                self.prepare_frame(pd.read_csv(os.path.join(startpath,filename), header=header, **kwargs),
                               xcol=xcol, ycols=ycols, labels=labels, yrcols=yrcols, yrlabels=yrlabels,
                               yr2cols=yr2cols, yr2labels=yr2labels, xerrors=xerrors,
                               yerrors=yerrors,
                               xaxislabel=xaxislabel, yaxislabel=yaxislabel,
                               yraxislabel=yraxislabel, yr2axislabel=yr2axislabel)

    def fit(self, deg=1):
        """fit the data usying a polynomial, store a fit of the data and the errors in self.fits.
        It also prints to the terminal the fit paramaters and errors

        Parameters
        ----------
        deg : int, optional
            The degree of the polynomial to be fit.
        """
        for data in self.yset:
            z, cov = np.polyfit(data[0], data[1], cov=True, deg=deg)
            try:
                if deg==1:
                    print('y=m*x+c, (m, c): ',z, '(dc, dm): ',np.sqrt(np.diag(cov)))
                else:
                    print(z, np.sqrt(np.diag(cov)))
            except:
                print(z)
            span = max(data[0]-min(data[0]))
            x = np.arange(min(data[0])-span/12.0, max(data[0])+span/12.0, span/100)
            y = np.poly1d(z)
            self.fits.append([x, y(x), z, cov])

    def smooth(self, window_len=5, window='blackman'):
        """smooth all of the yset data. Window length must be an odd number. By default it uses
        the blackman window which is 0 on the end. That means a value of window_len = 5 or greater
        is required to actualy do some smoothing. This removes the pointer to the original data
        and replaces it with numpy arrays of the smoothed data

        Parameters
        ----------
        x: the input signal
        window_len: int optional,
            the dimension of the smoothing window; should be an odd integer
        window: str optional
            the type of window from 'flat', 'hanning', 'hamming', 'bartlett', 'blackman'
            flat window will produce a moving average smoothing. default is blackman
        """
        for data in self.yset:
            data[1] = smooth(data[1], window_len=window_len, window=window)


def smooth(x, window_len, window):
    """smooth the data using a window with requested size.

    This method is based on the convolution of a scaled window with the signal.
    The signal is prepared by introducing reflected copies of the signal
    (with the window size) in both ends so that transient parts are minimized
    in the begining and end part of the output signal.

    input
    -----
    x: the input signal
    window_len: the dimension of the smoothing window; should be an odd integer
    window: the type of window from 'flat', 'hanning', 'hamming', 'bartlett', 'blackman'
        flat window will produce a moving average smoothing.

    output
    ------
    the smoothed signal

    example
    -------
    t=linspace(-2,2,0.1)
    x=sin(t)+randn(len(t))*0.1
    y=smooth(x)

    see also
    --------
    numpy.hanning, numpy.hamming, numpy.bartlett, numpy.blackman, numpy.convolve
    scipy.signal.lfilter

    Parameters
    ----------
    x : TYPE
        Description
    window_len : TYPE
        Description
    window : TYPE
        Description

    Raises
    ------
    ValueError
    Description
    """

    if x.ndim != 1:
        raise ValueError("smooth only accepts 1 dimension arrays.")

    if x.size < window_len:
        raise ValueError("Input vector needs to be bigger than window size.")

    if window_len < 3:
        return x

    if not window in ['flat', 'hanning', 'hamming', 'bartlett', 'blackman']:
        raise ValueError(
            "Window is not one of 'flat', 'hanning', 'hamming', 'bartlett', 'blackman'")

    s = np.r_[x[window_len-1:0:-1], x, x[-1:-window_len:-1]]
    # print(len(s))
    if window == 'flat':  # moving average
        w = np.ones(window_len, 'd')
    else:
        w = eval('np.'+window+'(window_len)')

    y = np.convolve(w/w.sum(), s, mode='valid')
    return y[(window_len/2):-(window_len/2)]
