from setuptools import setup, find_packages

from typing import List

# function to return requirements lists

def get_requirements(file_path:str) -> List[str]:

    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [r.replace("\n", "") for r in requirements]

    return requirements


setup(
    name= ' machine learning project',
    version='0.0.1',
    author= 'Temidayo Oni',
    install_requires = get_requirements('requirements.txt'),
    packages= find_packages(),
    author_email='onitemidayo@gmail.com'

)
