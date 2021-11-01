MPint :: running in Spyder step-by-step
---------------------------------------

1. Go to the directory with your datafiles
	* pre-process/convert the datafiles to correct format if necessary
	* sample pre-processing PY-scripts are in demo dataset (above)
2. Prepare a *library* for given set of spectra
	* you may use an existing library or edit a
	  [library template](./pe.html)
	* the libraries are saved in MPint installation directory,
	  subdirectory lib
	* the MPint installation dir:
	  `pythonXXX/lib/site-packages/mpint/lib`
3. Prepare a *master script* for processing the datafiles <br>
	* you may just copy+paste existing script or edit this
	  [master script template](./01mpint.html)
	* we note that master script emloys the above-defined library
4. Run the *master script*
	* conventional name of master script: `01mpint.py`
	* conventional output filenames: `01mpint.py.txt/png`
