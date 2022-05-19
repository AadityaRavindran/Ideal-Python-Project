import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

with open('requirements.txt') as f:
    requirements = f.read().splitlines()

with open('test_requirements.txt') as f:
    test_requirements = f.read().splitlines()

setuptools.setup(
    name="ring-lord",
    version="0.0.1",
    author="Aaditya Ravindran",
    description="Sample python module",
    long_description=long_description,
    long_description_content_type="text/markdown",
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    install_requires=requirements,
    test_suite="test_lord_of_the_rings",
    tests_require=test_requirements,
    packages=["lord_of_the_rings"],
    include_package_data=True,
    zip_safe=False,
    entry_points={
        'console_scripts': [
            'ring-lord = lord_of_the_rings.the_one_ring:main',
        ],
    },
    python_requires='>=3.7',
)
