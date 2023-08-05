from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in bajo_tierro/__init__.py
from bajo_tierro import __version__ as version

setup(
	name="bajo_tierro",
	version=version,
	description="Custom App Two",
	author="Sameer",
	author_email="sameer2mshaikh@gmail.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
