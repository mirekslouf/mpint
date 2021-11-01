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

1. Go to the directory with datafiles
	* for testing, you may use datafiles from our [demo directory](../demo)
	* pre-process/convert the datafiles to correct format if necessary
	* sample pre-processing scripts are part of the archive in [demo directory]
2. Copy file *01mpint.py* to the directory with datafiles
	* 01mpint.py = master script that runs the whole MPint calculation
	* 01mpint.py can be copied from previous MPint processing or demo directory 
	* alternatively, you can copy&edit the following
	  [master script template](./01mpint.html)
3. Run *01mpint.py* and see the results in the active directory

(2) Processing spectra, for which you need new library
------------------------------------------------------

This is more general case: <br>
We need to define which peaks to integrate and which indexes to calculate.

1. Prepare a new library
	* the easiest is to edit a [template](./pe.html)
	* the editing instructions are part of the template
	* save the edited file with different filename and PY-suffix
2. Save the newly prepared file = PY-library to MPint installation directory
	* MPint installation directory will be in Python directory
	* somewhere in subdirectory: *lib/site-packages/mpint*
	* this seems to be a hardcore, but it works fine
3. Proceed with the rest of MPint calculation like in the case (1) above