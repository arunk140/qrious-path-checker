def findNextPath(maze: list, pos: tuple, endPos: tuple, path: list) -> list:
    if pos in path:
        return path

    if getMazeSymbol(maze, pos) == 'x':
        return path

    if getMazeSymbol(maze, pos) == 's' or getMazeSymbol(maze, pos) == '.':
        path.append(pos)
    
    offsets = [ # up, down, left, right (2D Offsets)
        (0, 1),
        (0, -1),
        (1, 0),
        (-1, 0)
    ]

    # check all directions
    for offset in offsets:
        nextPos = (pos[0] + offset[0], pos[1] + offset[1])
        
        # check if nextPos is out of bounds
        if nextPos[0] < 0 or nextPos[0] >= len(maze) or nextPos[1] < 0 or nextPos[1] >= len(maze[0]):
            continue
        
        # check if nextPos is in path
        if nextPos in path:
            continue
    
        if nextPos == endPos: # stop if endPos is found
            path.append(nextPos)
            break

        path = findNextPath(maze, nextPos, endPos, path)
            
    return path
    
def splitAndTrimMaze(maze: str) -> list:
    # remove empty lines and spaces
    maze = maze.splitlines()
    maze = [list(line.strip()) for line in maze if line.strip()]
    return maze

def findStartAndEndCoords(maze: list) -> tuple:
    start = None
    end = None
    for i, line in enumerate(maze):
        if start is not None and end is not None:
            break
        if start is None and 's' in line:
            start = (i, line.index('s'))
        if end is None and 'e' in line:
            end = (i, line.index('e'))
    return start, end

def getMazeSymbol(maze: list, target: tuple) -> str:
    return maze[target[0]][target[1]]

def solvable(maze: str) -> bool:
    maze = splitAndTrimMaze(maze)
    start, end = findStartAndEndCoords(maze)
 
    # quick solve condition
    if start is None or end is None:
        return False

    path = [] # empty path initially
    path = findNextPath(maze, start, end, path) # init path with start as current position

    if end in path:
        return True
    else:
        return False


if __name__ == "__main__":
    maze1 = """
    xx.exx
    ...xxx
    .x....
    xxxx..
    x.x..s
    """
    maze2 = """
    xs.x.e
    ...x..
    """
    print(solvable(maze1))
    print(solvable(maze2))