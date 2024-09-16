from setuptools import find_packages, setup
from typing import List

HYPHEN_E_DOT = '-e .'

def get_requirements(file_path:str)->List[str]:

    """Parses a requirements file and returns a list of requirements"""

    requirements = []

    with open(file_path, 'r') as f:
        requirements = [line.strip() for line in f.readlines() if line.strip()]
    
    if HYPHEN_E_DOT in requirements:
        requirements.remove(HYPHEN_E_DOT)

    return requirements

setup(
    name='mlproject',
    version='1.0.0',
    packages=find_packages(),
    install_requires=get_requirements("requirements.txt"),
    author='Md Shamsad Alam',
    author_email='shamshad@example.com',
)