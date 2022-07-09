from copy import copy
maze = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 2, 1, 1, 0, 1, 0, 1, 0, 1],
    [1, 0, 0, 0, 0, 1, 0, 0, 0, 1],
    [1, 0, 1, 1, 0, 0, 0, 1, 0, 1],
    [1, 0, 0, 1, 0, 1, 0, 1, 3, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
]

def printMaze(maze):
    for row in maze:
        for col in row:
            print(col, end=" ")
        print()


def findVertices(maze, row, col):

    vertices = []

    if row > 0 and maze[row-1][col] != 1:
        vertices.append((row-1, col))

    if row < len(maze)-1 and maze[row+1][col] != 1:
        vertices.append((row+1, col))

    if col > 0 and maze[row][col-1] != 1:
        vertices.append((row, col-1))

    if col < len(maze[0])-1 and maze[row][col+1] != 1:
        vertices.append((row, col+1))

    return vertices


def solveMaze(maze, sRow, sCol, path):

    temp = copy(path)
    temp.append((sRow, sCol))

    if maze[sRow][sCol]==3:
        return temp

    vertices = findVertices(maze, sRow, sCol)

    for row,col in vertices:

        if (row,col) not in temp:
            res = solveMaze(maze, row, col, temp)
            if res:
                return res
        

    return None

print("Maze:")
printMaze(maze)

print()

print("Log: ")
res = solveMaze(maze,1,1,[])

print()

print("Path:")
print(res)

print()

print("Solved Maze:")
if res:
    for i,j in res:
        maze[i][j] = 'P'

    printMaze(maze)
