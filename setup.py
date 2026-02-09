"""GUI Agent - Text-to-Image GUI Generation and Evaluation Toolkit."""

import setuptools

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

setuptools.setup(
    name="gui-agent",
    version="0.1.0",
    author="GUI Agent Contributors",
    description="GUI generation and evaluation toolkit for mobile/desktop UI screenshot synthesis",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/anthropic/gui-agent",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.8",
    install_requires=[
        "pillow>=9.0.0",
        "requests>=2.28.0",
        "openai>=1.0.0",  # For GPT-4o evaluation
    ],
    extras_require={
        "dev": [
            "pytest>=7.0.0",
            "pytest-cov>=4.0.0",
            "black>=22.0.0",
            "flake8>=4.0.0",
        ],
    },
    entry_points={
        "console_scripts": [
            "gui-agent-generate=gui_agent.cli:generate",
            "gui-agent-evaluate=gui_agent.cli:evaluate",
        ],
    },
)
