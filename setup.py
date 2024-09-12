from setuptools import find_packages, setup


Hypen_E_Dot='-e .'


def get_requirements(file_path):
    requirements=[]
    with open(file_path,'r') as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("\n"," ") for req in requirements]
        if Hypen_E_Dot in requirements:
            requirements.remove(Hypen_E_Dot)
    return requirements


setup(
    name='MLProject',
    packages=find_packages(),
    version='0.0.1',
    description='A short description of the project.',
    author='Kobalan M',
    author_email="kobalanm2705@gmail.com",
    install_requires=get_requirements('requirements.txt')
)
