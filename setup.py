from setuptools import setup ,find_packages
from typing import List 

requirements = []
HYPHEN_E_DOT = '-e .'

def get_requirements(filepath : str) -> List[str]: 

    with open('requirements.txt') as file_obj : 
        requirements = file_obj.readlines()
        requirements = [ req.replace("\n" , "") for req in requirements]

        if HYPHEN_E_DOT in requirements : 
            requirements.remove(HYPHEN_E_DOT)


        return requirements 
    
 
setup( 
    name = "Data Extractor" , 
    version = "1.0.0" , 
    author= "Shavilya Rajput" , 
    author_email= "shavilyarajput50@gmail.com", 
    packages=  find_packages(),
    install_requires=get_requirements("requirements.txt")
)