from setuptools import find_packages,setup

def get_requirements(file_path)

setup(
name='MLproject',
version='0.0.1',
author='Hriday'
author_email='hridaynagrani@gmail.com',
packages=find_packages(),
install_requires=get_requirements('requirements.txt'),


)
