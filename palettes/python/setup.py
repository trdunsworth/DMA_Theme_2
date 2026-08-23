from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="dma-palette",
    version="1.0.0",
    author="Dunsworth-Mann Analytics LLC",
    author_email="contact@dunsworth-mann.com",
    description="DMA Theme - Semantic color palettes for data visualization in Python",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/trdunsworth/DMA_Theme_2",
    project_urls={
        "Bug Tracker": "https://github.com/trdunsworth/DMA_Theme_2/issues",
    },
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Topic :: Scientific/Engineering :: Visualization",
        "Topic :: Multimedia :: Graphics",
    ],
    packages=find_packages(where=".", include=["dma_palette*"]),
    python_requires=">=3.8",
    install_requires=[
        "matplotlib>=3.5",
        "cycler>=0.11",
    ],
    extras_require={
        "seaborn": ["seaborn>=0.11"],
        "plotnine": ["plotnine>=0.10"],
        "all": ["seaborn>=0.11", "plotnine>=0.10"],
    },
    include_package_data=True,
    package_data={
        "": ["*.py"],
    },
)