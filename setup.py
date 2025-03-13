from setuptools import setup, find_packages

setup(
    name="tic_tac_toe",
    version="1.0.0",
    packages=find_packages(),
    install_requires=[
        "requests",
        "python-dotenv"
    ],
    entry_points={
        "console_scripts": [
            "tic-tac-toe=run:main",
        ],
    },
)
