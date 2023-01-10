"""
mpint.lib.pe
------------
* Library that defines peaks and indexes for IR spectra of PE. 
* Additionally, the library defines X and Y limits for plotting of spectra.
"""

# Technical notes:
# 1) Peaks are defined in a variable, as they are constant values.
# 2) Indexes are defined in a function, because they are calculated.
# -----
# * If we defined indexes in a variable,
#   the running of the module would raise Exception,
#   because the indexes are calculated from peak_areas,
#   which are not known at the moment = at the time of definition.

import numpy as np
from mpint.pvars import peak
from collections import OrderedDict

peaks = {
    'Std'      : peak(x_pos = 1370, x_min = 1330, x_max = 1400),
    'C=O'      : peak(x_pos = 1720, x_min = 1680, x_max = 1850),
    'C=C_960'  : peak(x_pos =  965, x_min =  950, x_max =  980),
    'C=C_910'  : peak(x_pos =  910, x_min =  900, x_max =  930),
    'PE_amorf' : peak(x_pos = 1303, x_min = 1275, x_max = 1330),
    'PE_cryst' : peak(x_pos = 1897, x_min = 1850, x_max = 1950)}
"""
* Variable `peaks` defines peaks for integration.
* It is a dictionary containing peak names and positions.
* The definition of `peaks` is best seen directly from the source code.        
"""

def calculate_indexes(peaks):
    """
    * Calculate indexes from peak areas.
    * The peaks are defined above in global variable `peaks`.
    * The indexes are defined below, within this function, as expressions.

    Parameters
    ----------
    peaks : dict
        * A global variable defined above in current library.
        * Basically, the peaks are defined by means boundaries on X-axis.
        
    Returns
    -------
    indexes : OrderedDict 
        * OrderedDict - in order to keep the order of indexes in outputs.
        * The OrderedDict contains expressions = definitions of indexes.
        * Typical access to these expressions/calculations is as follows:
            
    >>> import mpint.lib.pe as SAMPLE
    >>> OI = SAMPLE.calculate_indexes(peaks).[OI]
        
    """
    # Create empty ordered dictionary
    indexes = OrderedDict()
    # Calculate OI = oxidation index
    indexes['OI'] = peaks['C=O'].area / peaks['Std'].area
    # Calculate VI = trans-vinylene index
    indexes['VI'] = peaks['C=C_960'].area / peaks['Std'].area
    # Calculate CI = crystallinity index
    CA = peaks['PE_cryst'].area / peaks['PE_amorf'].area
    indexes['CI'] = CA / (CA + 1)
    # Correct for possible small negative values
    if indexes['OI'] < 0 : indexes['OI'] = -0.0001
    if indexes['VI'] < 0 : indexes['VI'] = -0.0001
    # Return calculated values
    return(indexes)

def x_limits_for_plotting(XYdata):
    """
    Define X-limits for plotting of spectra.
    
    Parameters
    ----------
    XYdata : 2D numpy array
        XY-data = data defining the spectrum.
    
    Returns
    -------
    xmin, xmax : X-limits for plotting of spectra
    
    How to define xmin, xmax?
    -------------------------
    The xmin and xmax values are usually just hard-coded
    in the function below.
    """
    xmin = 800
    xmax = 2200
    return(xmin,xmax)
    
def y_limits_for_plotting(XYdata):
    """
    Define Y-limits for plotting of spectra.
    
    Parameters
    ----------
    XYdata : 2D-numpy array
        XY-data = data defining the spectrum.
    
    Returns
    -------
    ymin, ymax : Y-limits for plotting of spectra
    
    How to define ymin, ymax?
    -------------------------
    * If you know numpy well, you can define (ymin, ymax)
      in the code of this function below; this may give you nicer output.
    * If unsure, use the following (universal) code to define (ymin, ymax):
    
    >>> xmin,xmax = x_limits_for_plotting(XYdata)
    >>> ymin = np.min(XYdata[1,(xmin < XYdata[0]) & (XYdata[0] < xmax)]) * 0.9
    >>> ymax = np.max(XYdata[1,(xmin < XYdata[0]) & (XYdata[0] < xmax)]) * 1.1
    >>> return(ymin,ymax)
    """
    # Get X-limits for plotting
    xmin,xmax = x_limits_for_plotting(XYdata)
    # Calculate Y-limits for plotting
    # ymin = minimal Y-value between xmin,xmax (multiplied by 0.9)
    ymin = np.min(XYdata[1, (xmin < XYdata[0]) & (XYdata[0] < xmax)]) * 0.9
    # ymax = maximal Y-value in selected areas (multiplied by 1.1)
    ymax = max(
        np.max(XYdata[1, (1300 < XYdata[0]) & (XYdata[0] < 1400)]),
        np.max(XYdata[1, (1650 < XYdata[0]) & (XYdata[0] < 1800)])
        ) * 1.1
    # Return final values of ymin,ymax
    return(ymin,ymax)
