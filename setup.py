from setuptools import setup, find_packages
import os

version = open("VERSION.txt").read().strip()

setup(name='wrd.ubumirrors',
      version=version,
      description="Find fastest local ubuntu mirror",
      long_description=open("README.txt").read() + "\n" +
                       open(os.path.join("docs", "HISTORY.txt")).read(),
      # Get more strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
      classifiers=[
        "Programming Language :: Python",
        ],
      keywords='',
      author='Wes Turner',
      author_email='wes.turner@gmail.com',
      url='http://pypi.python.org/pypi/wrd.ubumirrors',
      license='New BSD',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['wrd', 'wrd.ubumirrors'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          # -*- Extra requirements: -*-
          'BeautifulSoup==3.0.8.1',
          'httping',
      ],
      entry_points={
      # -*- Entry points: -*-
          'console_scripts': [
            'ubumirrors = wrd.ubumirrors:main',
          ]
      },
      )
