from setuptools import find_packages,setup#for importing of things 
from typing import List

HYPHEN_E_DOT="-e ."

def get_requirements(file_path:str)->List[str]:
    '''
    this function will return the list of requiremnts 
    '''
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("\n","") for req in requirements]

        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)
    return requirements

setup(
    name='mlproject',
    version='0.0.1',
    author='Anish',
    author_email='anishswarnakar57@gmail.com',
    packages=find_packages(),#very important and very powerfull as it findes the packages there . Whenever the setup.py the find_package is running then it will see in how many folder it will have the __init__. It will directly consider this src as a package itself and it will try to build this . and when it builds then we can import this anywhere
    install_requires=get_requirements('requirements.txt')
)