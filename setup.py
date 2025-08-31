from setuptools import setup, find_packages

setup(
    name="climate_calculus",
    version="0.2.0",
    packages=find_packages(),
    install_requires=[
        "numpy",
        "pandas",
    ],
    entry_points={
        "console_scripts": [
            "climate-sim=climate_calculus.cli:main",
        ],
    },
)
