python
import subprocess
import sys
from setuptools import setup, find_packages

def install(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])

def uninstall(package):
    subprocess.check_call([sys.executable, "-m", "pip", "uninstall", package, "-y"])

def test_installation():
    try:
        import calculator
        assert True
    except ImportError:
        assert False

def test_version():
    setup_data = setup(
        name="calculator",
        version="0.1",
        packages=find_packages(),
        install_requires=[
            "pytest>=7.3.1",
            "pytest-cov>=4.1.0",
        ],
    )
    assert setup_data['version'] == '0.1'

def test_required_packages():
    try:
        import pytest
        import pytest_cov
        assert True
    except ImportError:
        assert False

if __name__ == "__main__":
    test_installation()
    test_version()
    test_required_packages()