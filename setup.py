import setuptools

with open("README.md", "r",encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="Dominate_Layui", 
    version="0.0.1-5",
    author="BM-Business-Dev-Liu",
    author_email="Liubaolin20070125@outlook.com",
    description="A packages for Dominate.Make your websiteuse Layui.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/BugMaker-project/Dominate_Layui",
    packages=["Dominate_Layui",
              "Dominate_Layui/static",
              "Dominate_Layui/static/Layui",
              "Dominate_Layui/static/Layui/css",
              "Dominate_Layui/static/Layui/css/modules",
              "Dominate_Layui/static/Layui/css/modules/layer",
              "Dominate_Layui/static/Layui/css/modules/laydate",
              "Dominate_Layui/static/Layui/css/module/layer/default",
              "Dominate_Layui/static/Layui/css/modules/laydate/default",
              "Dominate_Layui/static/Layui/font",
              "Dominate_Layui/static/Layui/images",
              "Dominate_Layui/static/Layui/images/face",
              "Dominate_Layui/static/layui/lay",
              "Dominate_Layui/static/layui/lay/modules"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: Microsoft ",
    ],
    python_requires='>=3',
)
