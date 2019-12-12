# Homework 3 by Nelson Su 10/1/2019
# Course: CS 4500
# This program uses turtle graphics to paint blobs onto a painting. It takes in the grid size, N, and the number of
# paintings to do, K, as user inputs. This will allow the program to set up a grid of N * N dimensions. Then it will
# produce an array of 0's of the same dimensions and start randomly choosing a point or cell in the grid to increment
# by 1. This will keep track of which cell has been painted and how many times. At the same time, turtle graphics
# is used to draw colored circles to imitate paint blobs at a position that corresponds to the array index. Paint
# blobs will continue to paint until all cells have been painted at least once. This will conclude a single painting.
# Afterwards, the array and painting resets and the game cycles until it meets the desired number of paintings.
# Once all paintings have been completed, data calculated from the paintings will be used to determine the
# min, max, and avg of paint blobs it took to paint a picture and blobs per cell. These statistics are displayed
# on the screen.

# Paint color guide:
# - Black = No paint
# - Yellow = Currently Painting
# - Blue = Has paint

import sys
import random
import turtle

blob = turtle.Turtle()
blob.speed(10)


# Function for setting up grid with number of cells per side as parameter
def set_grid(n):
    for i in range(n):
        for j in range(n):
            blob.color("black")
            blob.begin_fill()
            blob.pensize(10)
            blob.penup()
            blob.goto(i * 50, j * 50)
            blob.pendown()
            blob.circle(10)
            blob.end_fill()


# Function for painting at specific coordinates using array indexes as parameter
def paint(a, b):
    blob.color("yellow")
    blob.begin_fill()
    blob.pensize(10)
    blob.penup()
    blob.goto(a * 50, b * 50)
    blob.pendown()
    blob.circle(10)
    blob.end_fill()

    blob.color("blue")
    blob.begin_fill()
    blob.pensize(10)
    blob.penup()
    blob.goto(a * 50, b * 50)
    blob.pendown()
    blob.circle(10)
    blob.end_fill()


# Accepting an input for grid size and validating it
goodInputN = False
while not goodInputN:
    try:
        N = int(input("Enter an integer from 2 to 15 for a square grid size: "))
        goodInputN = True
        if N < 2 or N > 15:
            print("Invalid input. Try again.\n")
            goodInputN = False
    except:
        print("Invalid input. Try again.\n")
        N = False

# Accept an input for number of paintings and validating it
goodInputK = False
while not goodInputK:
    try:
        K = int(input("Enter an integer from 1 to 10 for number of paintings: "))
        goodInputK = True
        if K < 1 or K > 10:
            print("Invalid input. Try again.\n")
            goodInputK = False
    except:
        print("Invalid input. Try again.\n")
        goodInputK = False

complete = False
finishCount = 0
paintings = 1
totalBlobsArray = []
blobsPerCellArray = []

# Data structure for operating the game and drawing paint blobs using turtle
while paintings < K + 1:
    print("Setting up the grid...")
    set_grid(N)
    Matrix = [[0 for x in range(N)] for y in range(N)]
    print("Painting...")
    totalBlobs = 0

    while not complete:
        finishCount = 0
        xIndex = random.randint(0, N - 1)
        yIndex = random.randint(0, N - 1)

        Matrix[xIndex][yIndex] += 1
        paint(xIndex, yIndex)
        totalBlobs += 1

        for i in range(N):
            for j in range(N):
                if Matrix[i][j] > 0:
                    finishCount += 1
        if finishCount >= (N * N):
            complete = True
            for i in range(N):
                for j in range(N):
                    blobsPerCellArray.append(Matrix[i][j])
            input("Painting #" + str(paintings) + " is completed.\nPress Enter to continue...\n")
    paintings += 1
    complete = False
    blob.reset()
    totalBlobsArray.append(totalBlobs)

input("All paintings are completed.\nPress Enter for results...\n")

# Display to screen min, max, and avg of paint blobs it took to paint a picture and per cell
print("Minimum paint blobs it took to paint a picture: " + str(min(totalBlobsArray)))
print("Maximum paint blobs it took to paint a picture: " + str(max(totalBlobsArray)))
print("Average paint blobs it took to paint a picture: " + str(sum(totalBlobsArray) / K))

print("Minimum paint blobs per cell: " + str(min(blobsPerCellArray)))
print("Maximum paint blobs per cell: " + str(max(blobsPerCellArray)))
print("Average paint blobs per cell: " + str(sum(blobsPerCellArray) / (N * N * K)))

# print(Matrix)
# turtle.done()
