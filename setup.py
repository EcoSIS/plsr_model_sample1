import os
from setuptools import setup

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = "plsr_model_sample1",
    version = "0.0.1",
    author = "jrmerz@ucdavis.edu",
    description = ("this is a test, this is only a test"),
    license = "MIT",
    keywords = "testing test test",
    url = "http://ecosml.org",
    packages=[
        'plsr_model_sample1',
        'plsr_model_sample1.examples',
        'plsr_model_sample1.main'
    ],
    package_data={'plsr_model_sample1.coefficients' : 'plsr_model_sample1/coefficients'}
    long_description=read('README.md'),
    classifiers=[
        "License :: OSI Approved :: MIT License",
    ],
)