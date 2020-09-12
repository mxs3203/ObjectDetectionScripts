# This script merges categories. Going through Annotations folder (input path) 
# and merging neutrophil_low and high as same class, also removing bg class

import xml.etree.ElementTree as ET
import sys
import glob
import os

from pathlib import Path


if (len(sys.argv) == 0):
    print("Please input hte annotation folder")
else:
    ANN_DIR = sys.argv[1]
    print(ANN_DIR)

for f in glob.glob(ANN_DIR + "*.xml"):

    tree = ET.parse(f)
    root = tree.getroot()
    for parent in root.findall('object'):
        for item in parent.findall('name'):
            if item.text == 'neutrophil_low':
                item.text = 'neutrophil'
            if item.text == 'neutrophil_high':
                item.text = 'neutrophil'
            if item.text == 'bg':
                root.remove(parent)

    Path(ANN_DIR + "../AfterAnnPreprocess/").mkdir(parents=True, exist_ok=True)
    tree.write(ANN_DIR + "../AfterAnnPreprocess/" + os.path.basename(f))
