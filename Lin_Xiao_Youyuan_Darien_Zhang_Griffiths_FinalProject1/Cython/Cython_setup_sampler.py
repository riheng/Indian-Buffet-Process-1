
from distutils.core import setup, Extension
from Cython.Build import cythonize
import numpy as np

ext = Extension("Cython_sampler",
                sources=["Cython/Cython_sampler.pyx"],
                include_dirs=[np.get_include()],
                libraries=["m"],
                extra_compile_args=["-w",  "-std=c99"])

setup(name = "Cy_sampler",
      ext_modules = cythonize(ext),
     include_dirs=[np.get_include()])