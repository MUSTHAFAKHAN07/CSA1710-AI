class VacuumCleaner:
    def __init__(self, grid):
        self.grid = grid
        self.rows = len(grid)
        self.cols = len(grid[0])
        self.row = 0
        self.col = 0

    def clean(self):
        while True:
            self.clean_current_cell()
            if not self.move_to_next_cell():
                break

    def clean_current_cell(self):
        if self.grid[self.row][self.col] == 1:
            print(f"Cleaning cell at row {self.row}, col {self.col}")
            self.grid[self.row][self.col] = 0

    def move_to_next_cell(self):
        if self.row < self.rows - 1:
            self.row += 1
        elif self.col < self.cols - 1:
            self.row = 0
            self.col += 1
        else:
            return False
        return True

if __name__ == "__main__":
    # Define a grid where 1 represents a dirty cell
    grid = [[1, 0, 1],
            [0, 1, 0],
            [1, 0, 1]]

    # Create a vacuum cleaner agent and start cleaning
    vacuum = VacuumCleaner(grid)
    vacuum.clean()

