# python
# -*- coding: utf-8 -*-
import codecs
import os
import re
import sys

from setuptools import find_packages, setup
"""
linux:
rm -rf "dist/*";rm -rf "build/*";python3 setup.py bdist_wheel;python2 setup.py bdist_wheel;twine upload "dist/*;rm -rf "dist/*";rm -rf "build/*""
win32:
rm -rf dist;rm -rf build;python3 setup.py bdist_wheel;python2 setup.py bdist_wheel;twine upload "dist/*"
rm -rf dist;rm -rf build;rm -rf frequency_controller.egg-info
"""

py_version = sys.version_info
install_requires = []

if py_version.major == 2:
    install_requires.append("futures")

with codecs.open("README.md", encoding="u8") as f:
    long_description = f.read()

here = os.path.abspath(os.path.dirname(__file__))
with codecs.open(
        os.path.join(here, 'frequency_controller', '__init__.py'),
        encoding="u8") as f:
    version = re.search(r'''__version__ = ['"](.*?)['"]''', f.read()).group(1)

setup(
    name="frequency_controller",
    version=version,
    keywords=("frequency limitation async multi-thread asyncio asynchronous"),
    description=
    "Setting a limitation for usage frequency. Read more: https://github.com/ClericPy/frequency_controller.",
    long_description=long_description,
    long_description_content_type='text/markdown',
    license="MIT License",
    install_requires=install_requires,
    py_modules=["frequency_controller"],
    python_requires=">=2.7",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        'Programming Language :: Python',
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
    ],
    author="ClericPy",
    author_email="clericpy@gmail.com",
    url="https://github.com/ClericPy/frequency_controller",
    packages=find_packages(),
    platforms="any",
)
