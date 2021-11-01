MPint :: integration of peaks in multiple spectra
-------------------------------------------------

* The MPint package **reads series of spectra**...
	* saves each spectrum as PNG image
	* **integrates peaks** defined by the user
	* **and calculates indexes** defined by the user.
* Explanation of key terms:
	* Series of spectra = set of XY-files (ascii files with two columns: X,Y)
	* User-defined peaks = peaks are defined by minimum and maximum X-values
	* User-defined indexes = indexes are defined as ratios between peak areas
	* Example: IR oxidation index = (area of C=O peak) / (area of standard peak)
* Simple user definition of peaks and indexes:
	* Both peaks and indexes are defined in a very simple PY-library.
    * Editing/adjusting libraries is quite easy - see the documentation.
	* Once the library is defined, all calculations are fully automatic.

Installation
------------

* MPint is a standard Python package, deposited at
  [PyPI](http://pypi.org/projects/mpint)
* Consequently, it is installed with a single command: `pip install mpint`
* It should work with any Python >=3.6 distribution that includes
  [SciPy](https://www.scipy.org/) modules.

Documentation, help, examples, demo...
--------------------------------------

* **Simple introductory demo:**
	* Just download [sample data](./demo), run the scripts and see the results.
* **Running MPint in Spyder:**
	* [Printscreen](./images/mpint-in-spyder.png)
	  illustrating a typical MPint session in Spyder
	* [Spyder](https://www.spyder-ide.org/)
	  is a freeware Python IDE, usable as a simple UI, because...
		* it is easy to install: `pip install spyder`
		* it is well-established, standard, and user-friendly
		* you can see the program run, text and graphical outputs together
	* In general, the MPint session consists of four steps:
		* Go to the directory with your datafiles
			* pre-process/convert the datafiles to correct format if necessary
			* sample pre-processing PY-scripts are in demo dataset (above)
		* Prepare a *library* for given set of spectra
			* you may use an existing library or edit a simple
			  [library template]
			* the libraries are saved in MPint installation directory,
			  subdirectory lib
			* the MPint installation dir:
			  `pythonXXX/lib/site-packages/mpint/lib`
		* Prepare a *master script* for processing the datafiles <br>
			* you may just copy+paste existing script or edit this
			  [master script template]
			* we note that master script emloys the above-defined library
		* Run the *master script*
			* conventional name of master script: `01mpint.py`
			* conventional output filenames: `01mpint.py.txt/png`
* **Running MPint in other environments:**
	* Command line: quite Ok (analogous to Spyder).
	* Jupyter notebook: possible, but it brings no apparent benefits.
* **Detailed MPint documentation:**
	* all functions have docstrings, which enables the following...
	* Spyder: navigate your cursor to a function definition and press Ctrl+I
	* Pdoc: auto-generates
	  [HTML help](./pdoc.html/mpint/index.html)
	  which documents all functions, modules...

## Brief history

* Old versions of MPINT: Perl + GNUplot; work fine, not not too user-friendly 
* Version 1.0 = re-written in Python, tested on datafiles from CZ, IT, ES
