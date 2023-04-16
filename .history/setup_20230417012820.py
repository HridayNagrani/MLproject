import imp
from setuptools import find_packages,setup
from typing import List

def get_requirements(file_path:str)->List[str]:
    '''
    this func will return list of requirements

    '''
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        [for req in requi]

setup(
name='MLproject',
version='0.0.1',
author='Hriday'
author_email='hridaynagrani@gmail.com',
packages=find_packages(),
install_requires=get_requirements('requirements.txt'),


)
