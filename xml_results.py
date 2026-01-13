# load libs
import xml.etree.ElementTree as ET
import os.path
import mspy

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
        tree = ET.parse(self.path)
        root = tree.getroot()
        masses = []
        seqs = []
        for child in root:
            if "hits" in child.tag:
                for hit in child:
                    if "hit" in hit.tag:
                        if int(hit.get('number')) == 1:
                            for protein in hit:
                                for item in protein.iter():
                                    if "pep_exp_mz" in item.tag:
                                        mass = float(item.text)
                                        masses.append(mass)
                                    elif "pep_seq" in item.tag:
                                        seq = item.text
                                        seqs.append(seq)
        counter = 0
        peaks=[]
        for mass in masses:
            peak = obj_peak.peak(mass, pepSeq= seqs[counter])
            peaks.append(peak)
            counter += 1
        results = obj_peaklist.peaklist(peaks)
        return results