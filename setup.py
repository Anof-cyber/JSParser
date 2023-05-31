#!/usr/bin/env python
from setuptools import setup, find_packages

setup(
    name='JSParser',
    version='1.0',
    packages=find_packages(),
    description="",
    long_description=open('README.md').read(),
    author='Ben Sadeghipour',
    url='https://github.com/nahamsec/JSParser',
    install_requires=['safeurl', 'tornado==5.1', 'jsbeautifier==1.8.0',
                      'netaddr', 'pycurl==7.43.0.2', 'BeautifulSoup4'],
    python_requires='2.7',
)
