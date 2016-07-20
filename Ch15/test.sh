#!bin/bash
cat inputFile.txt | python mrMeanMapper.py
echo
cat inputFile.txt | python mrMeanMapper.py | python mrMeanReducer.py
echo
cat inputFile.txt | python mrMean.py --mapper
echo
cat inputFile.txt | python mrMean.py
echo
cat inputFile.txt | python mrMean.py >> outFile.txt
echo
cat kickStart.txt | python mrSVM.py