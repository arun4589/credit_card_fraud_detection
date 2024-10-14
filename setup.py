from setuptools import setup,find_packages
from typing import List



def get_requirements(file_path:str)->List[str]:
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace('\n','') for req in requirements]
        return requirements
    

setup(
    name='Credit_card_fraud_detection',
    author='Arun',
    author_email='erarunkumawat50@gmail.com',
    version='0.0.1',
    packages=find_packages(),
    install_requires=get_requirements('requirement.txt')

)


