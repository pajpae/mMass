# Main Tasks: Import Mascot results and show matched peaks AA seq either in the peak sidebar or in the spectrum viewer
Jab's idea for a main task. Might need a bit of scope research. Revision possible.

# Prerequisite for Main 1: Fix Plot not correctly refreshing on any user input apart from resizing
Problem description: 
In plot_canvas.py from l 131 onwards functions mostly use quickRefresh() instead of refresh(); test for onMMotion() using refresh works for Mouse Movement while on Plot.

Issues:
1. **Fixed!** Just replacing quickRefresh() with refresh() redraws plot without consideration for zoom, as parameter fullsize is not correctly set.

Fixes:  
1. Potential: Check for current plot size/zoom state before refresh() and hand over parameter to refresh().

Solved:
1. Kept parameter dc from quickRefresh() in refresh(); removing the parameter solved the unzooming issue. Fullsize parameter is correctly set by default.

# Prerequisite for Main 2: Fix mMass not correctly reading .mgf input files
Problem description:  
In parser_mgf.py an issue in l 165 occurs due to string byte incompatibility