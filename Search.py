from collections import defaultdict, deque

def find_viable_paths(file_path):
    # Read the input file
    with open(file_path, 'r', encoding='utf-8') as file:
        input_text = file.read()

    # Parse the input
    grid = defaultdict(dict)
    start = None

    for line in input_text.strip().split('\n'):
        symbol, x, y = line.split()
        x, y = int(x), int(y)
        grid[x][y] = symbol

        if symbol == '*':
            start = (x, y)

    # Define valid moves
    moves = {
        '╔': [(0, 1), (1, 0)],
        '╗': [(0, 1), (-1, 0)],
        '╚': [(0, -1), (1, 0)],
        '╝': [(0, -1), (-1, 0)],
        '║': [(0, 1), (0, -1)],
        '═': [(1, 0), (-1, 0)],
        '╠': [(0, 1), (0, -1), (1, 0)],
        '╣': [(0, 1), (0, -1), (-1, 0)],
        '╦': [(0, -1), (1, 0), (-1, 0)],
        '╩': [(0, 1), (1, 0), (-1, 0)],
        '╬': [(0, 1), (0, -1), (1, 0), (-1, 0)],
        '*': [(0, 1), (0, -1), (1, 0), (-1, 0)]
    }
    all_directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    def bfs(start):
        queue = deque([(start, '')])
        visited = set()
        paths = []

        while queue:
            (x, y), path = queue.popleft()
            
            if (x, y) in visited:
                continue
            
            visited.add((x, y))
            symbol = grid[x][y]
            new_path = path + symbol

            if symbol.isalpha() and len(new_path) > 1:
                paths.append(new_path)
                if symbol != path[-1]:  # Continue only if this letter is different from the previous symbol
                    possible_moves = all_directions
                else:
                    continue
            elif symbol in moves:
                possible_moves = moves[symbol]
            else:
                continue

            for dx, dy in possible_moves:
                nx, ny = x + dx, y + dy
                if (nx, ny) in grid:
                    queue.append(((nx, ny), new_path))

        return paths

    return bfs(start)

# Example usage:
file_path = 'C:/Users/rwilc/OneDrive/Documents/GitHub/GithubTest/Data Annotation/message (1).txt'
viable_paths = find_viable_paths(file_path)

print(f"Number of viable paths: {len(viable_paths)}")
for i, path in enumerate(viable_paths, 1):
    print(f"Path {i}: {path}")