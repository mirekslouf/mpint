print('MPInt = automated integration of selected peaks in multiple spectra')

# This file is can be used as a template to run complete MPint calculation.
# * Before running this script, you need a library file describing spectra.
#    => see https://mirekslouf.github.io/mpint/run_in_spyder/spyder.html
# * Once you have the library, modify section [0] and run the script.
#   => the script can run from command line or within Spyder
#   => the output files will be in active directory

import sys
from pathlib import Path
import mpint, mpint.pvars, mpint.pio, mpint.integrate

print('[0] Define input parameters.')
# Define correct library with sample description.
from mpint.lib import pe as SAMPLE
# Define where are the datafiles = spectra.
DATAFILES = Path('.').glob('*.dat')

print('[1] Process all spectra:')
# Initialize an empty table for peak integration results.
table = mpint.pvars.table_of_results()
# Go through all spectra, plot spectra, integrate peaks and save results...
for datafile in DATAFILES:
     print(datafile.name)
     XYdata  = mpint.pio.read_spectrum(datafile)
     PNGimg  = mpint.pio.save_spectrum_as_png(datafile, XYdata, SAMPLE)
     peaks   = mpint.integrate.integrate_peaks(SAMPLE.peaks, XYdata)
     indexes = SAMPLE.calculate_indexes(peaks)
     table   = table.append_row(datafile.name, indexes)
     
print('[2] Save final results to files:')
# We save the final indexes as a table (TXT) and graph (PNG).
OUTPUT_TABLE = sys.argv[0] + '.txt' 
table.save_as_txt(OUTPUT_TABLE) 
print(OUTPUT_TABLE)
OUTPUT_GRAPH = sys.argv[0] + '.txt.png';
table.save_as_png(OUTPUT_GRAPH)
print(OUTPUT_GRAPH)