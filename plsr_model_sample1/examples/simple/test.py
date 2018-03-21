## import main source
from os import path
import sys, unittest
sys.path.append(path.join('..', '..'))

from pandas import read_csv
from pandas.testing import assert_frame_equal
from transform.normalize import transform
from main.model import run

def load(csv, folder='input'):
  dir, filename = path.split(__file__)
  return read_csv(path.join(dir, folder, csv))

class TestPackage(unittest.TestCase):

  def setUp(self):
    self.spectra = load('ExampleSpectra.csv')

  def test_model(self):
    self.spectra = transform(self.spectra)
    assert_frame_equal(self.spectra, load('ExampleSpectra_Normalized.csv', 'output'))

    result = run(self.spectra)
    assert_frame_equal(result, load('ExampleOutput_Predictions.csv', 'output'))

if __name__ == '__main__':
  unittest.main()