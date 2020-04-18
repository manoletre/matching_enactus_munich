# Enactus Munich Project - Applicant Matching software

If you want to learn more about Enactus Munich please head to [our website](http://muenchen.enactus.de/)

# Installation:
1. Make sure you have [Python3](https://www.python.org/downloads/), [Pipenv](https://github.com/pypa/pipenv) and Excel installed in your pc.
2. Clone this project
3. Install all dependencies with `pipenv install`
4. Now you are ready to go :) Make sure to allways start your local environment by running `pipenv shell` before running the `main` script

# Usage:
1. Export the priorities of the applicants to the `matching` excel under the `Hacker` sheet
2. Run `python ./ candidates` to build the list of all candidates
3. Sort the priorities of the challenges in the `candidates` Excel
4. Run the matching with `python ./ matching`
5. The results will appear in the console