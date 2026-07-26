from setuptools import find_packages,setup
from typing import List

hyfen="-e ."
def get_requirements(file_path:str)->List[str]:
    '''   
      this function will return the  list of requirements '''
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("\n"," ") for req in requirements]

        if hyfen in requirements:
            requirements.remove(hyfen)

    return requirements


setup(
name="ML-project",
version="0.0.1",
author="karthik",
author_email="rameshrameshsri5607@gmail.com",
packages=find_packages(),
install_requires=get_requirements("requirements.txt")
)