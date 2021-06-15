from distutils.core import setup
from Cython.Build import cythonize
import numpy

# Package meta-data.
NAME = "efficientdet"
DESCRIPTION = "EfficientDet model re-implementation. Keras and TensorFlow Keras."
URL = "https://github.com/adrianbouza/EfficientDet"
EMAIL = "abnaveira.dev@gmail.com"
AUTHOR = "xuannianz"
REQUIRES_PYTHON = ">=3.0.0"
VERSION = None

setup(
    name=NAME,
    version=about["__version__"],
    description=DESCRIPTION,
    long_description=long_description,
    long_description_content_type="text/markdown",
    author=AUTHOR,
    author_email=EMAIL,
    python_requires=REQUIRES_PYTHON,
    url=URL,
    ext_modules=cythonize("utils/compute_overlap.pyx"),
    include_dirs=[numpy.get_include()]
)
