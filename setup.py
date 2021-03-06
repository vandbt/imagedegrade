#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

setup(
	name= 'imagedegrade', # Application name:
	version= '0.1.6', # Version number

	author= 'Masayuki Tanaka', # Author name
	author_email= 'mastnk@gmail.com', # Author mail	

	url='https://github.com/mastnk/imagedegrade', # Details
	description='Image degradation library for python.', # short description
	long_description='Image degradation library for python.', # long description
	install_requires=[ # Dependent packages (distributions)
		'Pillow', 'numpy', 'scipy'
	],
	
	include_package_data=False, # Include additional files into the package
	packages=find_packages(),

	test_suite = 'tests',

	classifiers=[
		'Programming Language :: Python :: 3.6',
		'License :: OSI Approved :: MIT',
    ]
)

# uninstall
# % python setup.py install --record installed_files
# % cat installed_files | xargs rm -rf
# % rm installed_files

