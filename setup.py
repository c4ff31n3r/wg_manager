from setuptools import setup, find_packages

setup(
    name="wg_manager",
    version="2.2.1",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        "pyyaml",
    ],
    entry_points={
        "console_scripts": [
            "wg_manager=wg_manager.main:main",
        ],
    },
    author="Ruslan Krupitsa",
    description="CLI WireGuard manager",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    license="GPLv3",
    python_requires=">=3.8",
)
