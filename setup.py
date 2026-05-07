from pathlib import Path

from setuptools import find_packages, setup


README = Path(__file__).with_name("README.md").read_text(encoding="utf-8")

setup(
    name="claude-agent-core",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "anthropic",
        "python-dotenv",
        "rich",
    ],
    author="Informant254",
    description="High-performance, lightweight Python wrapper for Claude 3.5 Sonnet optimized for agentic workflows.",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/Informant254/claude-agent-core",
    license="MIT",
    include_package_data=True,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.7',
)
