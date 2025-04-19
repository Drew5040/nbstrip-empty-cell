from setuptools import setup, find_packages

setup(
    name="nbstrip-empty-cell",
    version="0.1.0",
    description="Remove empty cells from Jupyter notebooks (pre-commit hook)",
    author="Drew5040",
    packages=find_packages(),  
    entry_points={
        "console_scripts": [
            "nbstrip-empty-cell = remove_empty_cells.cli:main"
        ],
    },
    install_requires=["nbformat"],
    python_requires=">=3.6",
)
