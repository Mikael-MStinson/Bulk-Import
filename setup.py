from setuptools import setup

setup(
	name = 'bulk_import',
	version = '0.0.1',
	description = 'A collection of tools for importing classes and modules in bulk',
	py_modules = ["bulk_import"],
	package_dir = {'':'src'},
	classifiers = [
		"Programming Language :: Python :: 3",
		"Programming Language :: Python :: 3.6",
		"Programming Language :: Python :: 3.7",
		"License :: OSI Approved :: GNU General Public License v2 or later (GPLv2+)",
		"Operating System :: OS Independent",
		"Intended Audience :: Developers",
		"Development Status :: 1 - Planning",
	],
	url = "https://github.com/Mikael-MStinson/Bulk-Import",
	author = "Mikael Morrell-Stinson",
)