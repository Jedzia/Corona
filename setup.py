from setuptools import setup, find_packages

setup(
    name='Corona',
    version='1.0.0',
    package_dir={"": "src"},
    packages=find_packages(where='src'),
    url='https://github.com/Jedzia/Corona',
    license='MIT',
    author='Jedzia',
    author_email='jed69@gmx.de',
    description='Virus Calculation Framework'
)
