# toy-sqrt-package

A simple Python package that computes the square root of a nonnegative number.

## Installation

From GitHub:
pip install git+https://github.com/CHAEMIN04/toy-sqrt-package.git

From local:
pip install -e .

## Usage

from toy_sqrt_package import sqrt_operator

sqrt_operator(4)   # returns 2.0
sqrt_operator(0)   # returns 0.0
sqrt_operator(-4)  # raises ValueError with friendly message
