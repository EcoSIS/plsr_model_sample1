from pandas import *
from numpy import *

#################################### NOTES
"""
Example spectra are from AVIRIS imagery
Process:
    1) spectra are extracted row-wise,
    2) bad bands are set to zero,
    3) the square root of the sum of squares of the spectra calculated,
    4) the original spectrum divided by the result of 3)
    5) spectra written to an output CSV
"""
#################################### DEFAULTS

baseDir='D:/Aditya/_AIST/Data/'
saveDir='D:/Aditya/_AIST/Data/'



# Output filename for vector normalized spectra
outputName=saveDir+'ExampleSpectra_Normalized.csv'

#################################### PROCESS

def transform(spectra, args):

    # Sample raw AVIRIS spectra
    specs=read_csv(baseDir+'ExampleSpectra.csv')
    # CSV containing bad bands set to 1s
    bands=read_csv(baseDir+'Bands.csv')

    # Get bad band list (bad bands: IsBad==1, good bands: IsBad==0)
    badBands=bands['IsBad'].values

    # Initialize array to hold normalized spectra
    outMat=zeros(specs.shape)

    # ...for each spectrum:
    for i in specs.index:
        print i
        # Extract row
        iSpec=array(specs.ix[i][:])
        # Set bad bands to zeros
        iSpec[badBands==1]=0
        # Find sqrt of sum of squares of all values
        sSpec=sqrt(sum(iSpec**2))
        # Normalize spectrum
        nSpec=iSpec/sSpec
        # Store results
        outMat[i,:]=nSpec

    # Save normalized spectra to CSV
    outDF=DataFrame(columns=specs.columns, data=outMat)
    outDF.to_csv(outputName,index=False)
    print '...Done'
