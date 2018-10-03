import setuptools

with open('requirements.txt') as f:
    requirements = f.read().splitlines()

setuptools.setup(
    name="HyperAPI-Nitro",
    version="1",
    author="HyperCube",
    author_email="support@hypercube-research.com",
    description="HyperCube API for Nitro",
    long_description="HyperCube API for Nitro",
    long_description_content_type="text/markdown",
    url="https://github.com/HyperCube/HyperAPI",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    install_requires=requirements,
    include_package_data=True
)
