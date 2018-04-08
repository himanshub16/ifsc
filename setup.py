from setuptools import setup, find_packages
import sys, os


# DEFAULT_DATAFILE = os.path.abspath('../IFSC.json')
DEFAULT_DATAFILE = '../IFSC.json'

setup(
    name='ifsc',
    version='1.0.1',
    description='Utility for IFSC code',
    long_description='Another utility',

    classifiers=[  # Optional
        # How mature is this project? Common values are
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        'Development Status :: 3 - Alpha',

        # Indicate who your project is intended for
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',

        # Pick your license as you wish
        'License :: OSI Approved :: MIT License',

        # Specify the Python versions you support here. In particular, ensure
        # that you indicate whether you support Python 2, Python 3 or both.
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],

    keywords='ifsc banking india',
    author='Himanshu Shekhar',
    author_email='himanshushekharb16@gmail.com',
    url='https://github.com/razorpay/ifsc',
    py_modules=['ifsc'],
    packages=find_packages('.'),
    include_package_data=True,
    data_files=[('data', [DEFAULT_DATAFILE])],  # Optional
    license='MIT'
)