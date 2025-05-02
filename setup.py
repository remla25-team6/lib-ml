import os
from setuptools import setup, find_packages

# Read the version from 
version = os.getenv('VERSION', '0.0.0')

setup(
    name='my_package',
    version = version,
    packages = find_packages(where='src'),
    package_dir = {'': 'src'},
    install_requires=["nltk"]
)