from setuptools import setup

setup(
    name='wacky',
    version='0.1',
    packages=['wacky'],
    install_requires=[
        "yacs"
        ],
    python_requires='>=3.6',
    include_package_data=True,
    author='Aditya Ganeshan',
    author_email='adityaganeshan@gmail.com',
    description='A Python package for making excalidraw figures procedurally from python.',
    url='https://github.com/bardofcodes/wacky',
)
