from setuptools import find_packages, setup
from typing import List
def get_requirements()->List[str]:
     requirement_list:list[str]=[]
     return requirement_list
setup(
    name="sensor",
    version="0.0.2",
    author="iNeuron",
    author_email="cloud@ineuron.ai",
    packages=find_packages(),
    install_requires=get_requirements(),#["pymongo==4.2.0"],
)
