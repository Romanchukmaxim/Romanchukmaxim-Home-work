import numpy as np

def crazyshuffle(arr):
    for x in arr:
        np.random.shuffle(x)
    np.random.shuffle(arr)
    return(arr)


WIDTH = 312
HEIGHT = 400

WHITE = (255,255,255)
BLACK = (0,0,0)

testBoard = [[0 for x in range(4)] for x in range(4)]
testBoard4x = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 0]]
testBoardCorrect = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 0]]
testBoard4 = crazyshuffle([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 0]])

def inline():
    line = []
    for i in testBoard4:
        for n in i:
            line.append(n)
    return line
print(inline())

gridPos = (6,6)

cellSize = 75
gridSize = cellSize*4

