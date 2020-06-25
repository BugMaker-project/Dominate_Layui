import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="Dominate_Layui", 
    version="V0.1Beta",
    author="BM-Business-Dev-Liu",
    author_email="Liubaolin20070125@outlook.com",
    description="A packages for Dominate.Make your websiteuse Layui.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/pypa/sampleproject",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3",
        "Operating System :: Microsoft :: Windows ::Windows 10",
    ],
    python_requires='>=3',
)
