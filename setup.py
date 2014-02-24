try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

setup(
    name='pycrxlib',
    version='0.1',
    description='Integrates generation of .crx files with build systems',
    long_description='\n'.join((
        "Routines for programatically generating Google Chrome .crx files.",
        "Good for Python-based build tools e.g. Fabric, Ansible, Paver and ",
        "possibly others"))
    packages=('crx',),
    url='https://github.com/JacobOscarson/pycrxlib',
    author='Jacob Oscarson',
    author_email='jacob@plexical.com',
    license='MIT',
    classifiers=(
        'Topic :: Software Development :: Build Tools',
        'Intended Audience :: Developers',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ),
)
