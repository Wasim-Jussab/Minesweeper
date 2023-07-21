# Minesweeper

This is a Python program that implements a simple Minesweeper game. It takes a grid representing a minefield as input and calculates the number of adjacent mines for each cell in the grid.

## How It Works

The program consists of the following main functions:

1. `count_adjacent_mines(grid)`: Takes a 2D grid as input and returns a new grid with the count of adjacent mines for each cell. The grid is represented by a list of lists, where the '#' symbol represents a mine, and any other symbol represents an empty cell.

2. `is_valid_position(row, col)`: A helper function that checks if a given position (row, col) is valid within the grid (i.e., it lies within the bounds of the grid).

3. `count_mines(row, col)`: A helper function that calculates the number of adjacent mines for a given cell in the grid. It iterates over each direction using a predefined list of direction tuples.

## How to Use

1. Ensure you have Python installed on your machine.

2. Clone the repository to your local machine using the following command:

```bash
git clone https://github.com/wasim-jussab/minesweeper.git
```

3. Change to the project directory:

```bash
cd minesweeper
```

4. Modify the `grid` variable in the `count_adjacent_mines` function to represent your minefield. The grid should be a list of lists, where '#' represents a mine, and any other symbol represents an empty cell.

5. Run the program:

```bash
python minesweeper.py
```

6. The program will calculate the count of adjacent mines for each cell and display the new grid with the counts.

## Example Usage

Consider the following minefield grid:

```python
grid = [
    ["#", ".", ".", "#"],
    [".", ".", "#", "."],
    ["#", "#", ".", "."],
    [".", ".", ".", "."]
]
```

Running the program will yield the following output:

```
Count of adjacent mines:

[
    ['#', '2', '1', '#'],
    ['2', '4', '#', '3'],
    ['#', '#', '3', '2'],
    ['1', '2', '2', '1']
]
```

## Contributing

If you'd like to contribute to this project or report any issues, please feel free to open a pull request or submit an issue on the GitHub repository.
---
Created by [Wasim Jussab](https://github.com/wasim-jussab)
```
