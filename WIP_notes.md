# Task: Fix Plot not correctly refreshing on any user input apart from resizing
Notes:  
 In plot_canvas.py from line 131 onwards functions mostly use quickRefresh() instead of refresh(); test for onMMotion() using refresh works for Mouse Movement while on Plot.

Issues:
1. Just replacing quickRefresh() with refresh() redraws plot without consideration for zoom, as parameter fullsize is not correctly set.

Fixes:  
1. Potential: Check for current plot size/zoom state before refresh() and hand over parameter to refresh().

Solved:
1. Kept parameter dc from quickRefresh() in refresh(); deleting it solved the unzooming issue

