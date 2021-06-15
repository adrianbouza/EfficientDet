from distutils.core import setup
from Cython.Build import cythonize
import numpy
from setuptools import find_packages, setup, Command

# Package meta-data.
NAME = "efficientdet"
DESCRIPTION = "EfficientDet model re-implementation. Keras and TensorFlow Keras."
URL = "https://github.com/adrianbouza/EfficientDet"
VERSION = "1.0.0"
setup(
    name=NAME,
    description=DESCRIPTION,
    url=URL,
    version=VERSION,
    packages=find_packages(),
    ext_modules=cythonize("utils/compute_overlap.pyx"),
    include_dirs=[numpy.get_include()]
)
