from distutils.core import setup
from Cython.Build import cythonize
import numpy

# Package meta-data.
NAME = "efficientdet"
DESCRIPTION = "EfficientDet model re-implementation. Keras and TensorFlow Keras."
URL = "https://github.com/adrianbouza/EfficientDet"

setup(
    name=NAME,
    description=DESCRIPTION,
    url=URL,
    ext_modules=cythonize("utils/compute_overlap.pyx"),
    include_dirs=[numpy.get_include()]
)
