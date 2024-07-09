# setup.py

from setuptools import setup

setup(
    name='sclog',
    version='1.0',
    py_modules=['sclog'],
    install_requires=[
        # Add any dependencies here, if required
    ],
    entry_points={
        'console_scripts': [
            'sclog = sclog:main'
        ],
    }
)
