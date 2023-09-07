#It must be in the root directory to define your project and its dependencies

from setuptools import setup, find_packages

setup(
    name='project',
    version='0.1',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    install_requires=open('requirements.txt').readlines(),
    entry_points={
        'console_scripts': [
            'project = main:main'
        ]
    }
)