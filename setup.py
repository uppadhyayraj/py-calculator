from setuptools import setup, find_packages

setup(
    name="calculator",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        "pytest>=7.3.1",
        "pytest-cov>=4.1.0",
    ],
)
