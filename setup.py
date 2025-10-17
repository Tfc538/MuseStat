"""
Setup configuration for MuseStat.
"""

from setuptools import setup, find_packages
import json

# Read version from version.json
with open("version.json", 'r', encoding='utf-8') as f:
    version_data = json.load(f)
    version = version_data['version']

# Read long description from README
with open("README.md", 'r', encoding='utf-8') as f:
    long_description = f.read()

setup(
    name="musestat",
    version=version,
    author="Tim Gatzke",
    author_email="post@tim-gatzke.de",
    description="Manuscript Statistics Analyzer with Advanced Features for Fiction Writers",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Tfc538/MuseStat",
    project_urls={
        "Homepage": "https://tim-gatzke.de",
        "Bug Reports": "https://github.com/Tfc538/MuseStat/issues",
        "Documentation": "https://github.com/Tfc538/MuseStat/blob/main/docs/INDEX.md",
        "Source": "https://github.com/Tfc538/MuseStat",
    },
    packages=find_packages(),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Intended Audience :: End Users/Desktop",
        "Topic :: Text Processing",
        "Topic :: Utilities",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.12",
        "Programming Language :: Python :: 3.13",
        "Programming Language :: Python :: 3.14",
    ],
    python_requires=">=3.7",
    install_requires=[
        "rich>=13.0.0",
        "questionary>=2.0.0",
        "python-docx>=0.8.11",
        "striprtf>=0.0.26",
        "langdetect>=1.0.9",
        "textstat>=0.7.3",
        "requests>=2.28.0",
    ],
    entry_points={
        'console_scripts': [
            'musestat=musestat.cli.commands:main',
        ],
    },
    include_package_data=True,
    zip_safe=False,
)

