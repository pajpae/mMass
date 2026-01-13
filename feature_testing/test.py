from csv_results import csvResults
from xml_results import xmlResults

filepathcsv = "c:/Users/ppaer/OneDrive/Documents/GitHub/mMass/feature_testing/test_data/FTGmmrEEt.csv"
filepathxml = "C:/Users/ppaer/OneDrive/Documents/GitHub/mMass/feature_testing/test_data/FTGmmrEEt.xml"

#results = csvResults(filepathcsv)
#results.getResults()

results = xmlResults(filepathxml)
test = results.getResults()