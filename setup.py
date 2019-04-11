#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import re
from setuptools import setup
import os

GMUSICPROXYFILE = 'GMusicProxy'
version_line = open(GMUSICPROXYFILE).read()
version_re = r"programVersion = ['\"]([^'\"]*)['\"]"
match = re.search(version_re, version_line, re.M)
if match:
    version = match.group(1)
else:
    raise RuntimeError("Could not find version in '%s'" % GMUSICPROXYFILE)

setup(
    name='gmusicproxy',
    version=version,
    author='Jeff M. Hubbard',
    author_email='jeffmhubbard@gmail.com',
    url='https://github.com/jeffmhubbard/gmusicproxy',
    scripts=[GMUSICPROXYFILE],
    license=open('LICENSE').read(),
    description='Google Play Music Proxy - "Let\'s stream Google Play Music using any media-player"',
    long_description=(open('README.md').read()),
    install_requires=['gmusicapi>=12.0.0', 'netifaces>=0.10.9',
                      'eyeD3>=0.8.10', 'python-daemon>=2.2.3',
                      'mutagen>=1.42.0', 'gpsoauth>=0.4.1',
                      'oauth2client>=4.1.3' if not os.name == 'nt' else ''],
)
