# Enactus Munich Project - Applicant Matching software

If you want to learn more about Enactus Munich please head to [our website](https://enactus-muenchen.de/)


# Installation:
1. Make sure you have [Python3](https://www.python.org/downloads/), [Pipenv](https://github.com/pypa/pipenv) and Excel installed in your pc.
2. Clone this project
3. Install all dependencies with `pipenv install`
4. Now you are ready to go :) Make sure to allways start your local environment by running `pipenv shell` before running the `main` script


# Tasks:
- Document usage of algorithm
	- add comments in the code
	- document that explains how it works in the background
- Export results to excel with explanation why
	- create forms with application requirements
	- script must work with variable number of application req.
- Test in TeamWE
- Go over algorithm with Juli (and Vorstand) to see what should be improved
	- and find someone with python knowledge to work with it


# How to use

## Before running
1. Make sure you have <code>pip</code> and <code>pipenv</code> installed in your pc. 
2. Run <code>pipenv install</code>. This will install all necessary dependencies on your local environment. 
3. Add all projects **as they are saved in the forms that are filled in** with the needed capacities to the *hospitals.xlsx* file. If a Key Error comes up, it is very likely that the project name is not well written.
4. Download the Excel for the candidates and paste the name in the <code>\_\_main\_\_.py</code> file as the parameter of the <code>Reader</code> instance. 

## Run
1. on the console in the root folder of the repository run <code>pipenv shell</code>. This activates the virtual environment. 
