# secureworks_challenge
Coding challenge from secure works

# Problem

Your code will be evaluated on the amount of test coverage and overall general quality too include readability, following best practices for the language, etc. Your code will be evaluated by more than one person, typically the hiring manager and potential future-coworkers that all completed a coding challenge before joining the team.  Please note they will execute their review based on the instructions you provide.

We advise using these best practices for your response:

- Provide working test cases
- Provide full documentation of everything in your response, to include assumptions
- Provide a set of instructions for the reviewers to execute their review
- Confirm the program runs out of the box before sending

## The Coding Challenge:

For this challenge, you can use node js, java, python, go, or whatever language you are most comfortable with, to develop code that meets the challenge requirements listed below:

1. Read input from a file of words
2. Find the largest word in the file
3. Transpose the letters in the largest word
4. Show the largest word and the largest word transposed 
5. Demonstrate positive and negative test cases
6. Ensure you document code and instructions for building and running based on the response best practices above

Example file (input)
```
a
ab
abc
abcd
abcde
```
Output
```
abcde
edcba
```

# Solution

This project provides solution to the problem

Assumptions
- The file is expected to be a text file ie., `.txt` extension
- The filepath is absolute to the project
- The script can process only one file at a time (No multi-threading)
- The standalone executable is a UNIX executable file, not tested in Windows


## Project Structure

```
secureworks_challenge
        |-- __init__.py
        |-- input_data/list_of_words.txt
        |-- transpose.py
        |-- tests
                |-- test_data
                        |-- empty_file.txt
                        |-- example_file.txt
                        |-- numbers_file.txt
                        |-- spaces_words.txt
                        |-- special_chars.txt
                |-- test_transpose.py
        |-- run_tests.sh
        |-- htmlcov
        |-- build
        |-- dist
                |-- transpose
        |-- Pipfile
        |-- Pipfile.lock
        |-- README.md
```
## Steps to run script

 - Clone the repository
 - Navigate to directory `secureworks_challenge/`

### Run script as standalone

Run the command
```
$ ./dist/transpose <path/to/inputfile>
```

### Run the script in virtualenv (pipenv)

#### Prerequsites
- `python >= 3.7.7`
- `pip >= 20.0.2`
- `pipenv >= 2018.11.26`

Launching virtualenv (pipenv)
- `$ pipenv shell`

Installing dependencies
- `$ pipenv install`

Running the script
- `$ pipenv run python transpose.py <path/to/inputfile>`

*NOTE*: For the example filepath, refer to `input_data/list_of_words.txt`

- `$ pipenv run python transpose.py input_data/list_of_words.txt`

## Steps to run tests

#### Prequisite

- Ensure the virtualenv (pipenv) is activated before running the tests

Run the command below:
- `$ sh run_tests.sh`

Coverage report in console
```
Name           Stmts   Miss  Cover   Missing
--------------------------------------------
transpose.py      26      1    96%   36
```
Coverage report in browser

- Navigate to `htmlcov` and open `index.html` in browser

----
## Author: Md Mahbubur Rahman








