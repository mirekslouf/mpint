"""
mpint.pio
---------
Package input/output functions.
"""

import numpy as np
import matplotlib.pyplot as plt

def read_spectrum(datafile):
    if datafile.suffix in ['.txt','.dat']:
        XYdata = np.loadtxt(datafile, unpack=True)
    elif datafile.suffix == ['.csv']:
        XYdata = np.loadtxt(datafile, separator=',', unpack=True)
    elif datafile.suffix == ['.spc']:
        raise NotImplementedError ('Reading of SPC not implemented yet.')
    return(XYdata)
        
def save_spectrum_as_png(datafile, XYdata, xmin=800, xmax=2200):
    # Determine Y-limits for the plot 
    ymin = np.min(XYdata[1, (xmin < XYdata[0]) & (XYdata[0] < xmax)]) * 0.9
    ymax = max(
        np.max(XYdata[1, (1300 < XYdata[0]) & (XYdata[0] < 1400)]),
        np.max(XYdata[1, (1650 < XYdata[0]) & (XYdata[0] < 1800)])
        ) * 1.1
    # Prepare the plot of spectrum
    plt.plot(XYdata[0],XYdata[1], color='red')
    plt.xlabel('Wavelength [1/cm]')
    plt.ylabel('Intensity')
    plt.xlim(xmin, xmax)
    plt.ylim(ymin, ymax)
    plt.grid()
    # Save the plot (output filename derived from datafile.name)
    output_filename = datafile.name + '.png'
    plt.tight_layout()
    plt.savefig(output_filename, dpi=100)
    # Close the plot (the next spectrum needs new/fress plot)
    plt.close()
