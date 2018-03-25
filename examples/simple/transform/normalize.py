from os import path
from pandas import DataFrame, read_csv
from numpy import sqrt, zeros, array

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
#################################### PROCESS

def load(csv):
    dir, filename = path.split(__file__)
    return read_csv(path.join(dir, '..', 'input', csv))

def transform(spectra):

    # Sample raw AVIRIS spectra
    # specs=read_csv(baseDir+'ExampleSpectra.csv')

    # CSV containing bad bands set to 1s
    bands=load('Bands.csv')

    # Get bad band list (bad bands: IsBad==1, good bands: IsBad==0)
    badBands=bands['IsBad'].values

    # Initialize array to hold normalized spectra
    outMat=zeros(spectra.shape)

    # ...for each spectrum:
    for i in spectra.index:
        # Extract row
        iSpec=array(spectra.ix[i][:])
        # Set bad bands to zeros
        iSpec[badBands==1]=0
        # Find sqrt of sum of squares of all values
        sSpec=sqrt(sum(iSpec**2))
        # Normalize spectrum
        nSpec=iSpec/sSpec
        # Store results
        outMat[i,:]=nSpec

    # Return normalized spectra dataframe
    return DataFrame(columns=spectra.columns, data=outMat)