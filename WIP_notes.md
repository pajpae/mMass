# Main Tasks: Import Mascot results and show matched peaks AA seq either in the peak sidebar or in the spectrum viewer
Jabs' idea for a main task. Might need a bit of scope research. Revision possible.

### Necessary functions  
1. 

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
Problem description: Apparently doesn't seem to work as well; haven't tested myself. Need to remind Jabs to upload a sample .mzxml

### Fully optional 1: Fix Spectrum Viewer not scrolling with arrow keys