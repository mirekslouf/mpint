MPint :: running in Spyder step-by-step
=======================================

(0) Introduction
----------------

For MPint processing, you need three things:

* [datafiles] = spectra = files with two columns
* [01mpint.py] = master script that runs the whole calculation  
* [library] = PY-formated file defining the peaks and indexes we want  

(1) Processing spectra with existing library
--------------------------------------------

This is quite frequent case: <br>
We process known spectra, for which the library has already been defined.  

1. Go to the directory with datafiles.
	* for testing, you may use datafiles from our [demo directory](../demo)
	* pre-process/convert the datafiles to correct format if necessary
	* sample pre-processing scripts are part of the archive in [demo directory]
2. Copy file `01mpint.py` to the directory with datafiles.
	* `01mpint.py` = master script that runs the whole MPint calculation
	* `01mpint.py` can be copied from previous MPint dir or [demo directory] 
	* alternatively, you can copy&edit the following
	  [master script template](./01mpint.html)
3. Open `01mpint.py` in Spyder and...
	* adjust section [0] as described in the [template](./01mpint.html)
	* run the script in Spyder and see the results on screen
	* the outputs are saved also in the current directory

(2) Processing spectra, for which you need a new library
--------------------------------------------------------

This is more general case: <br>
We need to define which peaks to integrate and which indexes to calculate.

1. Prepare the new library.
	* the easiest is to edit a [library template](./pe.html)
	* the instructions for editing/saving are part of the template
2. Proceed with the rest of MPint calculation like in the case (1) above.
