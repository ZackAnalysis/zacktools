import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="zacktools",
    version="0.3.8",
    author="Zack Dai",
    author_email="zdai@brocku.ca",
    description="Zack's ommon tools",
    long_description=long_description,
    long_description_content_type='text/markdown',
    url="https://github.com/ZackAnalysis/zacktools",
    classifiers=[
        "Programming Language :: Python :: 3.9",
        "Operating System :: OS Independent",
    ],
    packages=setuptools.find_packages(),
    install_requires=['bs4','lxml','pyap~=0.3.1','requests','aiohttp','aiohttp_requests','elasticsearch']
)