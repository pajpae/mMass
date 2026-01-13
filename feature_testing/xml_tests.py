import xml.etree.ElementTree as ET

filepathxml = "C:/Users/ppaer/OneDrive/Documents/GitHub/mMass/feature_testing/test_data/FTGmmrEEt.xml"
tree = ET.parse(filepathxml)
root = tree.getroot()
for child in root:
    if "hits" in child.tag:
        for group in child:
            if "hit" in group.tag:
                for item in group:
                    print(item.tag, item.attrib)