# load libs
import xml.etree.ElementTree as ET
import os.path
from . import mspy

# load stopper
from mspy.mod_stopper import CHECK_FORCE_QUIT

# load objects
from mspy import obj_peak
from mspy import obj_peaklist

# PARSE XML RESULTS
# --------------

class xmlResults:
    """Parse results from xml."""

    def __init__(self,path):
        self.path = path
        self.results = None
        self.pepmass = None
        self.pepseq = None

        # check path
        if not os.path.exists(path):
            raise IOError("File not found! --> " + self.path)
        
    # ----

    def getResults(self):
        pass