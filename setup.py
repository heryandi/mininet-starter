import os

from setuptools import setup, find_packages

scripts = [os.path.join('bin', filename) for filename in os.listdir('bin')] 

setup(
    name='mininet-starter',
    version='1.0.0',
    author='Heryandi',
    author_email='Heryandi@gmail.com',
    packages=find_packages(exclude='test'),
    scripts=scripts,
    url='https://github.com/heryandi/mininet-starter',
    license='MIT',
    description='Starter package to develop new Mininet modules',
    long_description=open('README.rst').read(),
    install_requires=[
        "mininet",
        "pip",
        "distribute",
    ],
    entry_points={'console_scripts': [
        'starter_console_script_1 = your_source_code:main',
        'starter_console_script_2 = your_source_code.utils:do_something',
    ]}
)
