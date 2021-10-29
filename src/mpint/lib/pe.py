"""
mpint.lib.pe
------------
Library that defines peaks and indexes in IR spectrum of PE. 
"""

# Technical notes:
# 1) Peaks are defined in a variable, as they are constant values.
# 2) Indexes are defined in a function, because they are calculated.
# -----
# * If we defined indexes in a variable,
#   the running of the module would raise Exception,
#   because the indexes are calculated from peak_areas,
#   which are not known at the moment = at the time of definition.

from mpint.pvars import peak
from collections import OrderedDict

peaks = {
    'Std'      : peak(x_pos = 1370, x_min = 1330, x_max = 1400),
    'C=O'      : peak(x_pos = 1720, x_min = 1680, x_max = 1850),
    'C=C_960'  : peak(x_pos =  965, x_min =  950, x_max =  980),
    'C=C_910'  : peak(x_pos =  910, x_min =  900, x_max =  930),
    'PE_amorf' : peak(x_pos = 1303, x_min = 1275, x_max = 1330),
    'PE_cryst' : peak(x_pos = 1897, x_min = 1850, x_max = 1950)}

def calculate_indexes(peaks):
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
