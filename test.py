from csv_results import csvResults
from xml_results import xmlResults

csvfilepath = "c:/Users/ppaer/OneDrive/Documents/GitHub/mMass/feature_testing/test_data/FTGmmrEEt.csv"

csvresults = csvResults(csvfilepath)
csvtest = csvresults.getResults()
print("\ncsvtest")
for peak in csvtest:
    print(peak.mz, peak.pepSeq)
xmlfilepath = "C:/Users/ppaer/OneDrive/Documents/GitHub/mMass/feature_testing/test_data/FTGmmrEEt.xml"
xmlresults = xmlResults(xmlfilepath)
xmltest = xmlresults.getResults()
print("\nxmltest")
for peak in xmltest:
    print(peak.mz, peak.pepSeq)
counter = 0
for peak in csvtest:
    other_peak = xmltest.peaks[counter]
    if peak.mz == other_peak.mz and peak.pepSeq == other_peak.pepSeq:
        print("yay")
    counter += 1