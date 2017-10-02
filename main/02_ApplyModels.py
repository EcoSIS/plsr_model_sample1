from pandas import *
from numpy import *

#################################### NOTES
"""
Example spectra are from AVIRIS imagery normalized using 01_Normalized.py
This code snippet implements getting predictions using
    1) A single set of coefficients
       ...get a single value per pixel/spectrum
    2) An array or coefficients
       ...get a mean and uncertainty per pixel/spectrum
"""
#################################### DEFAULTS

baseDir='D:/Aditya/_AIST/Data/'
saveDir='D:/Aditya/_AIST/Data/'

# Sample AVIRIS spectra normalized using 01_Normalized.py
specs=read_csv(baseDir+'ExampleSpectra_Normalized.csv')

# PLSR model coefficients
# ...one vector (only gets a mean value per pixel)
coefs_single=read_csv(baseDir+'PLSR_coefficients_Raw_Aggregated_Nitrogen.csv')
# ...array, gets mean and uncertainty per pixel)
coefs_multpl=read_csv(baseDir+'PLSR_coefficients_Raw_Full_Nitrogen.csv')

# Output CSVs
# ...will contain predictions for the single set, as well as for the one with multiple sets that produces uncertainties
outputCSV=saveDir+'ExampleOutput_Predictions.csv'

#################################### PROCESS

# Get coefficients
# ...single set
iCoef=array(coefs_single['mean'])
# ...array
mCoef=array(coefs_multpl)

# Get matrix of spectra
iSpec=array(specs)

# Add vector of ones to accomodate intercept
iSpec=hstack((ones((iSpec.shape[0],1)),iSpec))

# Matrix multiply iCoef and iSpec to get single vector of predictions
iPred=iSpec.dot(iCoef)

# Matrix multiply mCoef and iSpec to get multiple predictions
mPred=iSpec.dot(mCoef.T)
# ...aggregate predictions to get means and uncertainties
avePred=mPred.mean(axis=1)
stdPred=mPred.std(axis=1)

####################### Compile all into once CSV for comparison
outPreds=vstack((iPred,avePred,stdPred)).T
outDF=DataFrame(columns=['NIT_Single','NIT_MultMean','NIT_MultStdv'],data=outPreds)
outDF.to_csv(outputCSV,index=False)
print '...Done'

