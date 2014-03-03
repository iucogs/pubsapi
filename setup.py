# chardet's setup.py
from distutils.core import setup
import setuptools
setup(
    name = "pubs",
    packages = ["pubs"],
    version = "0.1",
    description = "IU COGS Pubs API",
    author = "IU Cognitive Science Program",
    author_email = "cogsci@indiana.edu",
    url = "http://pubs.cogs.indiana.edu/",
    download_url = "http://www.github.com/iucogs/pubs",
    keywords = ["bibliography", "academic"],
    classifiers = [
        "Programming Language :: Python",
        "Programming Language :: Python :: 2",
        "Development Status :: 4 - Beta",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Text Processing :: Linguistic",
        ],
    install_requires=[
        "SQLAlchemy>=0.7.0,<=0.7.99",
        "bottle>=0.12"
    ],

    long_description = """\
IU COGS Pubs
----------------------------------------------------------

Contains API interface for use with the IU Cognitive Science Program
Publications system, hosted at http://github.com/iucogs/pubs.
"""
)
