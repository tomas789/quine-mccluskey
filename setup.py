import os
import re
import subprocess
import sys
from glob import glob

from setuptools import setup

from pybind11.setup_helpers import Pybind11Extension, build_ext

ext_modules = [
    Pybind11Extension(
        "python_example",
        sorted(glob("src/*.cpp")),  # Sort source files for reproducibility
    ),
]


# The information here can also be placed in setup.cfg - better separation of
# logic and declaration, and simpler if you include description/version in a file.
setup(
    cmdclass={"build_ext": build_ext}, ext_modules=ext_modules,
)

