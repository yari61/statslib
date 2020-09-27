import setuptools

with open("requirements.txt", mode="r") as file:
    requirements = [line.split("#")[0] for line in file.read().split("\n") if not line.startswith("#")]

setuptools.setup(
    name="statslib",
    description="",
    version="0.0.1",
    packages=setuptools.find_packages(),
    install_requires=requirements
)
