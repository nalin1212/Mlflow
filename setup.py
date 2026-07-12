import setuptools

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()


__version__ = "0.0.0"

REPO_NAME = "End-to-end-ML-Project-with-MLflow"
AUTHOR_USER_NAME = "nalin_tiwari"
SRC_REPO = "mlProject"
AUTHOR_EMAIL = "nalin4835@gmail.com"


setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author="Nalin Tiwari",
    author_email="nalin4835@gmail.com",
    description="A small python package for ml app",
    long_description=long_description,
    long_description_content="text/markdown",
    url=f"https://github.com/nalin1212/Mlflow.git",
    project_urls={
        "Bug Tracker": f"https://github.com/nalin1212/Mlflow.git/issues",
    },
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src")
)