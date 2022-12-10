from glob import glob

from setuptools import setup
from pybind11.setup_helpers import Pybind11Extension, build_ext

ext_modules = [
    Pybind11Extension(
        "_quine_mccluskey_tomas789",
        sorted(glob("src_cpp/*.cpp")),
    ),
]

setup(
    packages=["quine_mccluskey_tomas789"],
    package_dir={"": "."},
    cmdclass={"build_ext": build_ext}, 
    ext_modules=ext_modules,
)

