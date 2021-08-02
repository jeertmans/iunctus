import setuptools

with open("README.md", "r") as f:
    long_description = f.read()


setuptools.setup(
    name="iunctus",
    version="0.0.1",
    author="Jérome Eertmans",
    author_email="jeertmans@icloud.com",
    description="Build an image-based network with you and the people appearing in pictures.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/jeertmans/iunctus",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    license="MIT",
    python_requires=">=3.8",
    entry_points={
        "console_scripts": [
            "iunctus = iunctus.cli.cli:iunctus",
        ]
    },
)
