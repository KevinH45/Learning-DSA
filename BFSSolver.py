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

def findPath(parent, end):

    path = []
    node = end

    while node:

        path.append(node)

        try:
            node = parent[node]
        except KeyError:
            break

    return path[::-1]

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

def solveMaze(maze):

    startRow, startCol = None, None
    endRow, endCol = None, None

    # Find the start and end point
    for row in range(len(maze)):
        for col in range(len(maze[0])):

            if maze[row][col] == 2:
                startRow = row
                startCol = col

            if maze[row][col] == 3:
                endRow = row
                endCol = col
    
    if not startRow or not endRow:
        print("Start or end point not found")
        return

    levelMap = {(startRow, startCol): 0}
    parent = {(startRow, startCol): None}
    level = 1
    frontier = [(startRow, startCol)]

    while frontier:

        nxt = []

        for row,col in frontier:
            
            for nRow, nCol in findVertices(maze, row, col):
                
                if (nRow,nCol) == (endRow, endCol):
                    print("Found the end")
                    parent[(nRow,nCol)] = (row,col)
                    return findPath(parent, (nRow, nCol))

                if (nRow,nCol) not in levelMap:
                    levelMap[(nRow,nCol)] = level
                    parent[(nRow,nCol)] = (row, col)
                    nxt.append((nRow,nCol))
        
        frontier = copy(nxt)
        level +=1
        
    print("Maze is not possible.")
    return


print("Maze:")
printMaze(maze)

print()

print("Log: ")
res = solveMaze(maze)

print()

print("Path:")
print(res)

print()

print("Solved Maze:")
if res:
    for i,j in res:
        maze[i][j] = 'P'

    printMaze(maze)
