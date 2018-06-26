import codecs
import os
import re
import sys

from setuptools import setup


here = os.path.abspath(os.path.dirname(__file__))


def read(*parts):
    # intentionally *not* adding an encoding option to open, See:
    #   https://github.com/pypa/virtualenv/issues/201#issuecomment-3145690
    with codecs.open(os.path.join(here, *parts), 'r') as fp:
        return fp.read()


def find_version(*file_paths):
    version_file = read(*file_paths)
    version_match = re.search(
        r"^__version__ = ['\"]([^'\"]*)['\"]",
        version_file,
        re.M,
    )
    if version_match:
        return version_match.group(1)

    raise RuntimeError("Unable to find version string.")


long_description = read('README.rst')


setup(
    name='dataclass-util',
    version=find_version('dataclass_util', '__init__.py'),
    description="Misc utils for dataclasses",
    long_description=long_description,
    license="MIT",
    url="https://github.com/betafcc/dataclass-util",
    author='Beta Faccion',
    author_email='betafcc@gmail.com',
    packages=['dataclass_util'],
)
