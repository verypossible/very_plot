#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""The setup script."""

import os
import sys
from setuptools import setup, find_packages
from setuptools.command.install import install

VERSION = '0.1.0'


class VerifyVersionCommand(install):
    """Custom command to verify that the git tag matches our version"""
    description = 'verify that the git tag matches our version'

    def run(self):
        tag = os.getenv('CIRCLE_TAG')

        if tag != VERSION:
            info = "Git tag: {0} does not match the version of this app: {1}".format(
                tag, VERSION
            )
            sys.exit(info)


with open('README.md') as readme_file:
    readme = readme_file.read()

with open('HISTORY.md') as history_file:
    history = history_file.read()

requirements = ['Click>=6.0', ]

setup_requirements = []

test_requirements = ['pytest']

setup(
    author="Jeff McGehee",
    author_email='jeff@verypossible.com',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
    description="Python plotting tools for Very",
    entry_points={
        'console_scripts': [
            'very_plot=very_plot.cli:main',
        ],
    },
    install_requires=requirements,
    license="GNU General Public License v3",
    long_description=readme + '\n\n' + history,
    include_package_data=True,
    keywords='very_plot',
    name='very_plot',
    packages=find_packages(include=['very_plot']),
    setup_requires=setup_requirements,
    test_suite='tests',
    tests_require=test_requirements,
    url='https://github.com/verypossible/very_plot',
    version=VERSION,
    zip_safe=False,
    cmdclass={
        'verify': VerifyVersionCommand,
    }
)
