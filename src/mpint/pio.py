"""
mpint.pio
---------
MPint input/output functions.
"""

import numpy as np
import matplotlib.pyplot as plt

def read_spectrum(datafile):
    """
    Read the spectrum from a datafile.
    
    Parameters
    ----------
    datafile : str or pathlib object
        * Name of the file from which the spectrum is read.
        * Datafile can be any file containing two columns = X and Y data.
        * Current version reads:
            - TXT-files and DAT-files = columns separated by spaces
            - CSV-files = comma-separated-values = columns separated by comma
    
    Raises
    ------
    NotImplementedError
        Exception, if datafile suffix/format is not known.

    Returns
    -------
    XYdata : 2D-numpy array
        Array containing two columns = spectrum = X-data and Y-data.
    """
    if datafile.suffix in ['.txt','.dat']:
        XYdata = np.loadtxt(datafile, unpack=True)
    elif datafile.suffix == ['.csv']:
        XYdata = np.loadtxt(datafile, separator=',', unpack=True)
    elif datafile.suffix == ['.spc']:
        raise NotImplementedError('Reading of SPC not implemented yet.')
    else:
        raise NotImplementedError('Unknown datafile suffix = unknown format.')
    # Important: XYdata = [wavelenghts,intensities]
    #   must be sorted in ascending order by the 1st column = wavelengths 
    # Reason   : this is assumed by method find_nearest below
    # Problem  : sometimes the wavelenght are sorted in descending order
    # Solution : if wavelenghts are descending, flip array using np.flip
    if XYdata[0,0] > XYdata[0,-1]: XYdata = np.flip(XYdata,1)
    # Return final data
    return(XYdata)
        
def save_spectrum_as_png(datafile, XYdata, SAMPLE):
    """
    Save spectrum in the form of PNG-graph.
    
    Parameters
    ----------
    datafile : str of pathlib object
        * Name of the file from which the spectrum was read.
        * This name is used for saving - output file name = [datafile].png
    XYdata : 2D-numpy array
        XYdata represent the spectrum = X-data and Y-data.
    SAMPLE : library name
        * The name of library describing given sample.
        * It is needed in order to determine X-limits/Y-limits for plotting.
        * The name of the library is imported in the main script as follows:
    
    >>> from mpint.lib import pe as SAMPLE
    
    Returns
    -------
    None.
        The output is the spectrum saved in the form of graph = PNG-file.
    """
    # Determine X-limits and Y-limits for the plotting of spectra.
    xmin,xmax = SAMPLE.x_limits_for_plotting(XYdata)
    ymin,ymax = SAMPLE.y_limits_for_plotting(XYdata)
    # Prepare the plot of spectrum (using the X/Y-limits determined above)
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
