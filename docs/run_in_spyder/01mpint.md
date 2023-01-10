MPint :: master script template
-------------------------------

* The template below can be employed as a *master script*
  that runs MPint calculation.
* The conventional name of the master script is `01mpint.py`
* If you keep the convention, the main outputs are `01mpint.py.txt/png` 
* Before running the script, you just modify two parameters in section [0]:
	* Name of the library desribing spectra of our sample <br>
	  the library (in the code below: pe) is imported as `SAMPLE`
	* Location of datafiles = files containing the individual spectra <br>
      the directory and filenames of the datafiles are in variable `DATAFILES`
* Concerning the libraries:
	* MPint is for batch processing - usually you use existing libraries
	* If you need to define new library, you can use a
	  [library template](../pe.html)

```python
print('MPInt = automated integration of selected peaks in multiple spectra')

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
```