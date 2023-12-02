# Python Arcade Sudoku Solver

## Overview
The Python Arcade Sudoku Solver is an application which permits a user to input numbers into a 9 X 9 puzzle grid. Upon clicking the "Solve" button, the program will iterate through possible solutions until it either finds one or determines the puzzle cannot be solved.

## Description

The Python Arcade Sudoku Solver can be played as a standalone Sudoku game, or it can be used, as the name implies, as a means by which an incomplete Sudoku puzzle may be solved, with the solution displayed in the puzzle grid. The game remembers which numbers are original, thus preventing a player from attempting to change them. These numbers are all colored red as an indication of their permanent state. All empty puzzle locations are available to populate with the numbers 1 - 9 or to clear of a user-entered number by pressing the space bar. When a user clicks on a location in the puzzle, the location is highlighted, indicating it is waiting for input. A buzzer will sound should the user attempt to select one of the original, red, unchangeable numbers. 

## Purpose

Over the years, I have worked on many, many Sudoku puzzles. Too often, I have been unable to solve them, particularly those deemed 'difficult' or 'impossible'. I decided to code this application to let me input a puzzle, work on it until I determined I could not solve it, and then run this to see what the solution might look like. I could also use it to give myself a hint, if needed. 

## Demo Video

The following is a video demonstration of the application functioning and a code walkthrough:

[Python Arcade Sudoku Solver Demo](http://youtube.link.goes.here)

# Development Environment

This application was developed using Microsoft's Visual Studio Code.

The programming language used to create this program was Python. It was configured with the Arcade library.

# Useful Websites

Here are a few websites which helped me understand how to utilize the Arcade library for Python:

* [The Python Arcade Library (Documentation/Tutorial)](https://api.arcade.academy/en/latest/)
* [Python Arcade - Basic Concepts (Video Tutorial Series)](https://www.youtube.com/playlist?list=PLP6KYkkXj-QbBP0He1Ot5wGgtPbR9hqxR)
* [Paul Vincent Craven - Easy 2D Game Creation With Arcade](https://www.youtube.com/watch?v=DAWHMHMPVHU)

# Future Work

While the application is functional, in the future I'd like to expand its capabilities. This will include:

* Allowing the game to load a puzzle (both an incomplete puzzle and with its solution)
* Allowing the game to save a puzzle (again, both an incomplete puzzle and with its solution)
* Making it possible for the user to play a Sudoku game and have it automatically check to see if a filled-in puzzle is solved, not just automatically solve the puzzle for the user (logic is written, but commented out, so this one may come next)
* Permitting the user to 'reset' the puzzle to its beginning when playing to solve
* Creating multiple difficulty levels for a user to play
* Creating the ability for the user to get hints as he or she plays it 
* Timing the user and setting up a 'High Scores' table based on difficulty and time to solution (Any hints given would invalidate the user appearing on the table)