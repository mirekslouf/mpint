## MPINT :: peak integration in multiple spectra

* The MPINT package **reads series of spectra**...
	* saves each spectrum as PNG image
	* **integrates peaks** defined by the user
	* **and calculates indexes** defined by the user.
* Explanation of key terms:
	* Series of spectra = set of XY-files (ascii files with two columns: X,Y)
	* User-defined peaks = peaks are defined by minimum and maximum X-values
	* User-defined indexes = indexes are defined as ratios between peak areas
	* Example: IR oxidation index = (area of C=O peak) / (standard peak area)
* Simple user definition of peaks and indexes:
	* Both peaks and indexes are defined in a very simple PY-library.
	* Every user can easily create and/or modify its own libraries.
	* Once the library is defined, all calculations are fully automatic.

## Installation

* MPint is a standard Python package.
* Consequently, it can be installed in a usual way: `pip install mpint`
* It should work with any [Python >=3.6 distribution]
  that includes [Scipy](https://www.scipy.org/) modules.
	
## Documentation, help, examples, demos...

* Complete documentation is at Github &rArr;
  [https://mirekslouf.github.io/mpint](https://mirekslouf.github.io/mpint)
  
## Brief history

* Old versions of MPINT: Perl + GNUplot; work fine, not not too user-friendly 
* Version 1.0 = re-written in Python, tested on datafiles from CZ, IT, ES
