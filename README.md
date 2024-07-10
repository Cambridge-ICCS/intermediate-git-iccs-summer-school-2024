# Intermediate Git and GitHub

## Assumed knowledge

In this course, we assume familiarity with the following Git commands and GitHub concepts:

* `add`, `commit`, `push`, `pull`, `log`
* Issues
* Pull requests (PRs)

If these are new to you then please join the
[*Introduction to Git and GitHub for Beginners* course][1], which is running in parallel.

## Accompanying slides

Please click
[here](https://hackmd.io/@jwallwork/2024-07-10-intermediate-git-tools?type=slide#/)
to access to the accompanying slides.

## The example code

This repository contains example code in a Python module `maths.py`. This module
contains a function for generating the equation of a line from two 2D points.
The repository also includes unit tests for this function in `test_maths.py`.

## Usage

To run code in this repository, you will need a working Python3 installation. We
recommend that you create a virtual environment for the purposes of this course.
To do this, run the following in a terminal window:
```
python3 -m venv /path/to/intergit
```
where `intergit` is the name of the virtual environment and a path should be
specified for where the virtual environment will be stored. To activate the
virtual environment, run
```
source /path/to/intergit/bin/activate
```
which should result in `(intergit)` appearing before your command prompt.

To install all dependencies into your virtual environment, navigate to the root
directory of your clone of this repository and run
```
python3 -m pip install -r requirements.txt
```

To test the example code, navigate to the root directory of your clone of this
repository and run
```
pytest -v test_maths.py
```

[1]: https://github.com/Cambridge-ICCS/git-intro-iccs-summer-school-2024
