import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="algorithms-shritwik",
    version="0.0.1",
    author="shritwik bhaduri",
    author_email="sritwikbhaduri@outlook.com",
    description="contain code for major data structures (basically specified in CLRS text book)",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/shritwikbhaduri/datastructures",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.8',
)
