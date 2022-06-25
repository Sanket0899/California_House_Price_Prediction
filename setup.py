from setuptools import setup
from typing import List

#DECLARING VARIABLES FOR SETUP FUNCTION
PROJECT_NAME='housing_predictor'
VERSION='0.0.1'
AUTHOR="Sanket"
DESCRIPTION='This is fsds nov first project'
PACKAGES=['Housing']
REQUIREMENT_FILE_NAME='requirements.txt'

def get_requirements_list() -> List[str]:
    """
    Description:This function is going to return list of requiremenets mention in the requiremnets.txt
    file

    return This function is goin to return a list which contains name of the libraries mentioned in the
    requirements.txt file
    """
    
    with open(REQUIREMENT_FILE_NAME) as requirement_file:
        requirement_file.readlines()

setup(
    name=PROJECT_NAME,
    version=VERSION,
    author=AUTHOR,
    description=DESCRIPTION,
    package=PACKAGES,
    install_requires=get_requirements_list()
)


