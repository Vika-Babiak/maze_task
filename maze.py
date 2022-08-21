def read_maze(file_name):
    """read a maze from a text file and represent it as 2d list"""

    # check if we can open and read the text file with a maze
    with open(file_name) as file_maze:
        maze = [[char for char in line.strip('\n')] for line in file_maze]
        return maze


maze = read_maze("maze.txt")

# print maze
for line in maze:
    print(line)


def get_points(list_):

    point_1 = ()
    point_2 = ()

    for i, value in enumerate(list_):
        if 'O' in value:
            j = value.index('O')
            point_1 = j, i
            value[j] = ' '
        if 'F' in value:
            j = value.index('F')
            point_2 = j, i
            value[j] = ' '

    return point_1, point_2


def grid(maze):

    # set start and end points
    start_pt, end_pt = get_points(maze)
    # print(f'start_point: {start_pt}')
    # print(f'end_point: {end_pt}')

    # check if maze is empty
    if len(maze) == 0:
        return f'The maze is empty'

    # check if there is only allowed symbols in the maze
    allowed_chars = [' ', 'X', 'O', 'F']
    for line_ in maze:
        for char in line_:
            if char not in allowed_chars:
                return f'There is an exceptable char in the maze: {char}'

    # use BFS algorythm to find the shortest path
    visited = {end_pt: None}
    queue = [end_pt]
    while queue:
        current = queue.pop(0)
        if current == start_pt:
            shortest_path = []
            while current:
                shortest_path.append(current)
                current = visited[current]
            return shortest_path
        adj_points = []

        # find adjacent points
        current_col, current_row = current

        # go up
        if current_row > 0:
            if maze[current_row - 1][current_col] == ' ':
                adj_points.append((current_col, current_row - 1))
        # go right
        if current_col < (len(maze[0]) - 1):
            if maze[current_row][current_col + 1] == " ":
                adj_points.append((current_col + 1, current_row))
        # go down
        if current_row < (len(maze) - 1):
            if maze[current_row + 1][current_col] == " ":
                adj_points.append((current_col, current_row + 1))
        # go left
        if current_col > 0:
            if maze[current_row][current_col - 1] == " ":
                adj_points.append((current_col - 1, current_row))

        #  loop through adjacent points
        for point in adj_points:
            if point not in visited:
                visited[point] = current
                queue.append(point)
    return f'no way found from: {start_pt} to: {end_pt}'

print(grid(maze))

# check a couple of cases
maze1 = [
    [' ', 'X', ' ', 'X', ' '],
    [' ', ' ', 'O', 'X', ' '],
    [' ', ' ', 'X', 'X', 'F'],
]
maze2 = [
    [' ', 'X', ' ', 'X', 'O'],
    [' ', ' ', 'X', ' ', ' ', ' '],
    [' ', 'F', ' ', ' ', 'X']
]

maze3 = []
maze4 = [
    [' ', 'X', ' ', 'X', 'O'],
    [' ', ' ', 'X', ' ', ' '],
    [' ', 'F', ' ', 'A', 'X']
]

assert grid(maze1) == 'no way found from: (2, 1) to: (4, 2)'
assert grid(maze2) == [(4, 0), (4, 1), (3, 1), (3, 2), (2, 2), (1, 2)]
assert grid(maze2) != [(4, 0), (4, 1), (3, 1), (3, 2), (2, 2)]
assert grid(maze3) == 'The maze is empty'
assert grid(maze4) == 'There is an exceptable char in the maze: A'
