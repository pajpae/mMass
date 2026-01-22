# Main Tasks: Import Mascot results and show matched peaks AA seq either in the peak sidebar or in the spectrum viewer

panel_peaklist.py has edits the peaklist to the right as a start to the work;
worked through to l 458 continue from there

### Necessary functions  
1. Input of Mascot Match .xml file into programm (automatization possible?)
2. Extraction of peptide sequences and masses from .xml
3. Application of the extracted data to the corresponding peaks

### Optional tasks
1. Connection to Mascot Server and starting a search

## Main Preparation
### Prerequisite for Main 1: Fix Plot not correctly refreshing on any user input apart from resizing
Problem description: 
In plot_canvas.py from l 131 onwards functions mostly use quickRefresh() instead of refresh(); test for onMMotion() using refresh works for Mouse Movement while on Plot.

Issues:
1. **Fixed!** Just replacing quickRefresh() with refresh() redraws plot without consideration for zoom, as parameter fullsize is not correctly set.

Fix Ideas:  
1. Check for current plot size/zoom state before refresh() and hand over parameter to refresh()

Solved:
1. Kept parameter dc from quickRefresh() in refresh(); removing the parameter solved the unzooming issue. Fullsize parameter is correctly set by default.

### Prerequisite for Main 2: Fix mMass not correctly reading .mgf input files
Problem description:  
In parser_mgf.py an issue in l 165 occurs due to string byte incompatibility

Issues:
1. **Fixed!** Converting the binary encoded line to string allows use of regex Pattern and Match methods to used but data is not displayed in spectrum viewer

Fix Ideas:
1. Debugger shows faulty deconstruction of string containing measurements likely due to falsely constructed regex pattern in l 124

Solved:
1. Corrected l 124 pattern for string splitting. Data correctly gets added to peaklist and by extension spectrum viewer  

### Prerequisite for Main 3: mMass needs to properly connect to Mascot Server from code  
Problem description: Trying to use Mascot Sever from code caused error (Server not responding)

### Optional for Main 1: Check if mMass .mzxml handling works
Problem description **Fixed!**:  
In mod_signal.py ll 524-525 there is a change to how the debugger works, which leads to an issue reading in the data. Deleting them solves the problem

### Fully optional 1: Fix Spectrum Viewer not scrolling with arrow keys