from setuptools import setup, find_packages

version = open("VERSION.txt").read().strip()

setup(
    name='pymirrortime',
    version=version,
    description="Check mirror response times",
    long_description=(open("README.rst").read() + "\n" +
                      open("HISTORY.rst").read()),
    # Get more strings from
    # http://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        "Programming Language :: Python",
        ],
    keywords='',
    author='Wes Turner',
    author_email='wes@wrd.nu',
    url='http://pypi.python.org/pypi/pymirrortime',
    license='New BSD',
    packages=find_packages(exclude=['ez_setup']),
    #namespace_packages=['pymirrortime'],
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'setuptools',
        # -*- Extra requirements: -*-
        'beautifulsoup4',
        'eventlet',
        ],
    entry_points={
        # -*- Entry points: -*-
        'console_scripts': [
            'ubumirrors = pymirrortime.ubuntu:main',
            'pymirrortime = pymirrortime.cli:main',
            'httping = pymirrortime.httping:main'
            ]
        },
    )
