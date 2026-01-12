# load libs
import csv
import os.path
import mspy

# load stopper
from mspy.mod_stopper import CHECK_FORCE_QUIT

# load objects
from mspy import obj_peak
from mspy import obj_peaklist

# PARSE CSV RESULTS
# --------------

class csvResults:
    """Parse results from csv."""

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
        # open document:
        peaks = []
        with open(self.path) as csvfile:
            csv_reader = csv.reader(csvfile, delimiter=',')
            blocker = True
            for row in csv_reader:
                if len(row) < 1:
                        continue
                elif blocker:
                    if row[0] == 'Protein hits':
                        blocker = False
                        continue
                    else:
                        continue
                if len(row) > 0:
                    counter = 0
                    if not self.pepmass and not self.pepseq:
                        while not self.pepmass and not self.pepseq:
                            for i in row:
                                if i == 'pep_exp_mz':
                                    self.pepmass = counter
                                elif i == 'pep_seq':
                                    self.pepseq = counter
                                counter += 1
                    else:
                        if int(row[0]) == 1:
                            obs_mz = float(row[self.pepmass])
                            pep_seq = (row[self.pepseq])
                            peak = obj_peak.peak(obs_mz, pepSeq = pep_seq)
                            peaks.append(peak)
                        else:
                            break
        results = obj_peaklist.peaklist(peaks)
        for peak in results:
            print (f"pepmass: {peak.mz}; pepseq: {peak.pepSeq}")