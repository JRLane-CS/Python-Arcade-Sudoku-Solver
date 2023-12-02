# Python Arcade Sudoku Solver

## Overview
The Python Arcade Sudoku Solver is an application which permits a user to input numbers into a 9 X 9 puzzle grid. Upon clicking the "Solve" button, the program will iterate through possible solutions until it either finds one or determines the puzzle cannot be solved.

## Description

The Python Arcade Sudoku Solver can be played as a standalone Sudoku game, or it can be used, as the name implies, as a means by which an incomplete Sudoku puzzle may be solved, with the solution displayed in the puzzle grid. The game remembers which numbers are original, thus preventing a player from attempting to change them. These numbers are all colored red as an indication of their permanent state. All empty puzzle locations are available to populate with the numbers 1 through 9 by highlighting a location and using the keyboard to input the number or to clear a location of a user-entered number by pressing the space bar. When a user clicks on a location in the puzzle, the location is highlighted, indicating it is waiting for input. If the user has filled in all locations, the application checks to see if the puzzle is solved or if the solution is incorrect and displays the message. If the user has tried to solve a puzzle he or she has worked on and failed, or if they merely want to start over, the application allows for a puzzle reset to starting position by pressing the ESC key.

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

* Allowing the game to load a puzzle 
* Allowing the game to save a puzzle 
* Creating multiple difficulty levels for a user to play
* Creating an option for the application to help a user complete a puzzle by making a buzzing noise if he or she tries to insert an incorrect number into a location
* Creating the ability for the user to get hints as he or she plays it by displaying small potential matches when the right mouse button is clicked in a location
* Timing the user and setting up a 'High Scores' table based on difficulty and time to solution