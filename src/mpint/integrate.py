"""
mpint.integrate
---------------
MPint functions for integration of all peaks.
""" 

def integrate_peaks(peaks, XYdata):
    """
    Integrate all peaks for given spectrum.
    
    Parameters
    ----------
    peaks : dict
        * Global variable defining all peaks = dictionary of `peak` objects.
        * The `peaks` variable is defined in a library such as `mpint.lib.pe`.
    XYdata : 2D-numpy array
        * Array with XY-data = X-data and Y-data = spectrum.
        * XY-data are read from datafiles containg two columns (X,Y).

    Returns
    -------
    peaks : updated global variable
        * After the update, `peaks` variable contains info about peak areas.
        * The updated `peaks` are employed
          in the subsequent calculation of indexes.
        * The calculation of indexes does not require a special function here,
          because it is defined directly within a library that describes
          given spectrum (example: `mpint.lib.pe.calculate_indexes`).
    """
    for k in peaks: peaks[k].integrate(XYdata)
    return(peaks)
