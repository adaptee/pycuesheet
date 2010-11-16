#!/usr/bin/env python
# vim: set fileencoding=utf-8 :

from distutils.core import setup

setup(  name="cuesheet",
        version="0.1",
        description="python module for parsing cuesheet data",
        requires=["ply"],
        packages=['cuesheet'],
        author="Jekyll Wu",
        author_email="adaptee@gmail.com",
        url="http://www.github.com/adaptee/pycuesheet",
     )
