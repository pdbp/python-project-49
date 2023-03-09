### Hexlet tests and linter status:
[![Actions Status](https://github.com/pdbp/python-project-49/workflows/hexlet-check/badge.svg)](https://github.com/pdbp/python-project-49/actions)
[![Maintainability](https://api.codeclimate.com/v1/badges/e1b5791c9aec70d2a3a1/maintainability)](https://codeclimate.com/github/pdbp/python-project-49/maintainability)

# Hexlet-code

The project contains 5 games for training logical and mathematical thinking.  

## Rules  

Each game offers answers to automatically generated questions. Each question assumes one of the answers: "yes" or "no". To win the game, you need to answer the questions correctly three times in a row. In case of an incorrect answer, the game ends and it must be started from the beginning.  

## Installation Instructions  

To install the game, go to the project folder and enter the command:  
Python version 3.6 or higher is required for the project to work. To check the Python version, use the command in the terminal:  
    `python3 --version`  

If Python is not installed, nstall it by typing in the terminal:  
    `sudo apt update`  
    `sudo apt install python3`  

You also need The Python Package Installer to work. To check the pip version, use the command:   
    `python3 -m pip --version`  

You will need version 19 and higher. If necessary, update pip with the command:  
    `python3 -m pip install --upgrade --user pip`  

If pip is not installed, install it by typing in the terminal:  
    `sudo apt update`  
    `sudo apt install python3-pip`  

To work, you need the poetry package manager version "1.2.0" and higher.  To check if Poetry is installed, type in the terminal:  
    `poetry --version`  
    
If Poetry is not installed, install it according to the instructions:  
    https://python-poetry.org/docs/  

Configure Poetry so that it creates virtual environments in the project directory. To do this, run the command:  
    `poetry config virtualenvs.in-project true`  

To start working with a project, copy it from the repository by entering the command:    
    `git clone git@github.com:pdbp/python-project-49.git`  

Install the package using the command (Poetry will create a virtual environment and install the package into it):  
    `make install`  

To build a package, use the following command:  
    `make build`  

To install the package from the operating system, use the following command:  
    `make package-install`  

## Launch Instructions  

To start the game, enter one of the commands:
- `brain-even` 
- `brain-calc` 
- `brain-gcd` 
- `brain-progression` 
- `brain-prime` 

## Demonstrations

brain-even: https://asciinema.org/a/BfY3Mi6QAnNV6hZXc7QIGaYUS  
brain-calc: https://asciinema.org/a/abszUwE5UONEAGYH9oyPpTBXx  
brain-gcd: https://asciinema.org/a/ripq1zQ1nxkx4GcXCa7Q2ZpUz  
brain-progression: https://asciinema.org/a/Z3Oa7GfchoK2I7uXk0e9K2Dlu  
brain-prime: https://asciinema.org/a/or2BC2Mrr9xzNiYwynCwIsuC7  
