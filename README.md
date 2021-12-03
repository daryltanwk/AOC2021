# Advent of Code 2021
A personal repo to store and run AOC solutions in python!

Advent of Code: https://adventofcode.com/2021

## Pre-requisites
1. Docker
2. I think that's about it?

## How to Use
### Setting Up
1. Log in to Advent of Code and grab your cookie session id
    - Open the Dev Console on your browser (<kbd>Ctrl</kbd>+<kbd>Shift</kbd>+<kbd>I</kbd> OR <kbd>F12</kbd>)
    - Under Storage Tab (I use Firefox. Interface varies with other browsers), look for Cookies on the Left Pane and find the session id
2. Clone this repo to wherever
3. Paste the session id into the `cookie_temp` file and rename it to `cookie`
4. Done!

### Getting Inputs for Day X
Run the following:
``` bash
# Getting Input file for Day 4
./getInput 4
```
This creates a folder `Day_4` and downloads the input file into the folder as `input_4`

<b>IMPT: Input values are different for each user!</b>

### Testing solutions
1. Place your main function into the appropriate `Day_X` folder and name it `aoc2021_X`.
    - For example, Day 4's solution should be in the `Day_4` folder and named as `aoc2021_4.py`
2. Run the `pyRun` script as such:
``` bash
# Test Day 4 Solution
./pyRun 4
```
