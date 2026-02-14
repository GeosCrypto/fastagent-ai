#!/usr/bin/env python3
"""
Setup script for FastAgent AI
"""

from setuptools import setup, find_packages
import os

# Read the README file for long description
def read_file(filename):
    with open(os.path.join(os.path.dirname(__file__), filename), encoding='utf-8') as f:
        return f.read()

setup(
    name='fastagent-ai',
    version='1.0.0',
    author='GeosCrypto',
    author_email='',
    description='A comprehensive AI agent for completing assignments and answering questions',
    long_description=read_file('README.md'),
    long_description_content_type='text/markdown',
    url='https://github.com/GeosCrypto/fastagent-ai',
    py_modules=['fastagent'],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Intended Audience :: Education',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Topic :: Education',
        'Topic :: Scientific/Engineering :: Artificial Intelligence',
    ],
    python_requires='>=3.7',
    install_requires=[
        # No external dependencies required for basic functionality
    ],
    extras_require={
        'dev': [
            'pytest>=6.0',
            'pytest-cov>=2.0',
        ],
    },
    entry_points={
        'console_scripts': [
            'fastagent=fastagent:main',
        ],
    },
    keywords='ai agent assistant education learning automation',
    project_urls={
        'Bug Reports': 'https://github.com/GeosCrypto/fastagent-ai/issues',
        'Source': 'https://github.com/GeosCrypto/fastagent-ai',
    },
)
