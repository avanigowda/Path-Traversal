from setuptools import setup, find_packages

setup(
    name="path_traversal_toolkit",
    version="1.0.0",
    packages=find_packages(),
    install_requires=[
        "requests",
        "argparse",
    ],
    entry_points={
        "console_scripts": [
            "path_traversal_toolkit = path_traversal_toolkit:main",
        ]
    },
)
 
