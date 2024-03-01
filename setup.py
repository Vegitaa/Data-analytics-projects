from setuptools import find_packages,setup
from typing import List

HYPEN_E_DOT='-e .'
def get_requirements(file_path:str)->List[str]:
    '''this function will return the list of requirenments
    '''
    requirenments=[]
    with open(file_path) as file_obj:
        requirenments=file_obj.readlines()
        requirenments=[req.replace("/n","")for req in requirenments]
        if HYPEN_E_DOT in requirenments:
            requirenments.remove(HYPEN_E_DOT)

    return requirenments
setup(
name='data analysis project',
version='0.0.1',
author='Pankaj Bhosale',
author_email='pankajbhosale7880@gmail.com',
packages=find_packages(),
install_requires=get_requirements('requirenments.txt')  
) 