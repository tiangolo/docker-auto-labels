#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""The setup script."""

from setuptools import setup, find_packages

with open('README.md') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = ['Click>=6.0', 'docker', 'pyyaml']

setup_requirements = ['pytest-runner']

test_requirements = ['pytest']

description = """Automatically generate Docker Swarm mode node
labels for each constraint label in each
service in a Docker Compose / Docker Stack file."""

setup(
    author="Sebastian Ramirez",
    author_email='tiangolo@gmail.com',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
    description=description,
    entry_points={
        'console_scripts': [
            'docker-auto-labels=docker_auto_labels.cli:main',
        ],
    },
    install_requires=requirements,
    license="MIT license",
    long_description=readme + '\n\n' + history,
    include_package_data=True,
    keywords='docker_auto_labels',
    name='docker_auto_labels',
    packages=find_packages(include=['docker_auto_labels']),
    setup_requires=setup_requirements,
    test_suite='tests',
    tests_require=test_requirements,
    url='https://github.com/tiangolo/docker_auto_labels',
    version='0.2.3',
    zip_safe=False,
)
