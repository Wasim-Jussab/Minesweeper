def count_adjacent_mines(grid):
    rows = len(grid)
    cols = len(grid[0])
    directions = [
        (-1, -1), (-1, 0), (-1, 1),
        (0, -1),           (0, 1),
        (1, -1),  (1, 0),  (1, 1)
    ]

    # Check if the given position is valid within the grid
    def is_valid_position(row, col):
        return 0 <= row < rows and 0 <= col < cols

    # Count the number of adjacent mines for the given position
    def count_mines(row, col):
        count = 0
        # Iterate over each direction to check neighbouring cells
        for dr, dc in directions:
            # Calculate the adjacent position
            adj_row = row + dr
            adj_col = col + dc
            # Check if the adjacent position is valid and contains a mine
            if is_valid_position(adj_row, adj_col) and grid[adj_row][adj_col] == "#":
                count += 1
        # Convert the count to a string and return it
        return str(count)

    # Create a new grid to store the counts
    new_grid = [[None] * cols for _ in range(rows)]
    # Iterate over each cell in the original grid
    for row, row_values in enumerate(grid):
        for col, cell in enumerate(row_values):
            # If the cell contains a mine, copy it directly to the new grid
            if cell == "#":
                new_grid[row][col] = "#"
            # If the cell is empty, count the adjacent mines and assign the count to the new grid
            else:
                new_grid[row][col] = count_mines(row, col)
    # Return the new grid
    return new_grid
