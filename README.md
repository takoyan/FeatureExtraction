# FeatureExtraction
## 1st step
cat FileName.json | awk 'NR > 1 {print}' > NewFile.json

## 2nd step
FeatureExtraction.py

## 3rd step
predLabel.py
