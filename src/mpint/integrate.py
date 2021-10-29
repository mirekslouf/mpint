def integrate_peaks(peaks, XYdata):
    for k in peaks: peaks[k].integrate(XYdata)
    return(peaks)
