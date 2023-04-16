from setuptools import find_packages,setup
from typo

def get_requirements(file_path:str)->List[str]:


setup(
name='MLproject',
version='0.0.1',
author='Hriday'
author_email='hridaynagrani@gmail.com',
packages=find_packages(),
install_requires=get_requirements('requirements.txt'),


)
