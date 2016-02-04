# -*- coding: utf-8 -*-
# (C) Copyright Digital Catapult Limited 2016

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


VERSION = "0.0.1"

setup(name="file-convert",
      version=VERSION,
      description=("Utility to convert the contents of a file by "
                   "running a set of regular expressions over it."),
      author="Digicat",
      packages=["file-convert"],
      entry_points="""\
      [console_scripts]
      file-convert = file-convert.convert:main
      """)
