import setuptools

with open("README.md", "r",encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="Dominate_Layui", 
    version="2020.6.25-1",
    author="BM-Business-Dev-Liu",
    author_email="Liubaolin20070125@outlook.com",
    description="A packages for Dominate.Make your website by Layui.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/BugMaker-project/Dominate_Layui",
    packages=["Dominate_Layui"],
    include_package_data=True,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: Microsoft ",
    ],
    python_requires='>=3',
)
