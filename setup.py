from pathlib import Path

this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text(encoding="utf-8")

from setuptools import setup, find_packages

setup(
    name="nbstrip-empty-cells",
    long_description=long_description,
    long_description_content_type="text/markdown",
    version="0.1.0",
    description="Remove empty code and markdown cells from Jupyter notebooks (ideal for pre-commit hooks)",
    author="Drew5040",
    packages=find_packages(),  
    entry_points={
        "console_scripts": [
            "nbstrip-empty-cell = remove_empty_cells.cli:main"
        ],
    },
    install_requires=[
        "nbformat>=5.1.4",
    ],
    python_requires=">=3.6",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Utilities",
    ],
    include_package_data=True,
)

