from setuptools import setup, find_packages

with open('README.rst', encoding='UTF-8') as f:
    readme = f.read()

setup(
    name="pgbackup",
    version="0.1.0",
    description="Database backups to AWS or locally",
    long_description=readme,
    install_requires=[],
    packages=find_packages('src'),
    package_dir={'':'src'}
)
