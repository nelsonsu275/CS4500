Homework 3 by Nelson Su 10/1/2019
Course: CS 4500
This program uses turtle graphics to paint blobs onto a painting. It takes in the grid size, N, and the number of
paintings to do, K, as user inputs. This will allow the program to set up a grid of N * N dimensions. Then it will
produce an array of 0's of the same dimensions and start randomly choosing a point or cell in the grid to increment
by 1. This will keep track of which cell has been painted and how many times. At the same time, turtle graphics
is used to draw colored circles to imitate paint blobs at a position that corresponds to the array index. Paint
blobs will continue to paint until all cells have been painted at least once. This will conclude a single painting.
Afterwards, the array and painting resets and the game cycles until it meets the desired number of paintings.
Once all paintings have been completed, data calculated from the paintings will be used to determine the
min, max, and avg of paint blobs it took to paint a picture and blobs per cell. These statistics are displayed
on the screen.

Paint color guide:
- Black = No paint
- Yellow = Currently Painting
- Blue = Has paint
