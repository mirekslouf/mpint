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
	* Example: IR oxidation index = (area of C=O peak) / (standard peak area)
* Simple user definition of peaks and indexes:
	* Both peaks and indexes are defined in a very simple PY-library.
    * Editing/adjusting libraries is quite easy - see the documentation.
	* Once the library is defined, all calculations are fully automatic.

Quick start
-----------
* Download [example1.zip](https://www.dropbox.com/scl/fo/7axsdxnw03us29r8r0p5w/h?rlkey=l2hs3948fi2u9olcxxnysswrd&dl=0)
* Unpack the data in a separate directory.
* Read the *readme* file in the main unpacked dir.
* Follow the instructions in *readme*, run the scripts and see the results.
* If you run the scripts in
  [Spyder](https://www.spyder-ide.org),
  the MPint session looks like
  [this](https://mirekslouf.github.io/mpint/docs/assets/spyder_prinscreen.png).

Documentation, help, and examples
---------------------------------
* [PyPI](https://pypi.org/project/mpint) repository.
* [GitHub](https://github.com/mirekslouf/mpint) repository.
* [GitHub Pages](https://mirekslouf.github.io/mpint/)
  with [documentation](https://mirekslouf.github.io/mpint/docs).

Brief history
-------------
* Old versions of MPINT: Perl + GNUplot; work fine, but not too user-friendly 
* Version 1.0 = re-written in Python, tested on datafiles from CZ, IT, ES
* Version 1.1 = small improvements of code + improved documentation

