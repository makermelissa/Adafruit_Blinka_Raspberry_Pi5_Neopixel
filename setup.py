# Available at setup time due to pyproject.toml
from pybind11.setup_helpers import Pybind11Extension, build_ext
from setuptools import setup
from setuptools_scm import get_version

__version__ = get_version()

# The main interface is through Pybind11Extension.
# * You can add cxx_std=11/14/17, and then build_ext can be removed.
# * You can set include_pybind11=false to add the include directory yourself,
#   say from a submodule.

ext_modules = [
    Pybind11Extension("neopixel_write_pi5",
        ["src/main.cpp", "src/utils/piolib/piolib.c", "src/utils/piolib/pio_rp1.c"],
        define_macros = [('VERSION_INFO', __version__)],
        include_dirs = ['./src/utils/piolib/include'],
        cxx_std = "20",
        extra_compile_args = ["-g3"],
        ),
]

setup(
    name="adafruit-blinka-neopixel-pi5",
    version=__version__,
    url="https://github.com/adafruit/adafruit-blinka-neopixel-pi5",
    description="Control NeoPixel & compatibles on a Pi 5",
    long_description="A pio-based driver",
    ext_modules=ext_modules,
    # Currently, build_ext only provides an optional "highest supported C++
    # level" feature, but in the future it may provide more features.
    cmdclass={"build_ext": build_ext},
    zip_safe=False,
    python_requires=">=3.11",
)
