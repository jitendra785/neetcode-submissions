class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # validate rows
        for row_idx in range(9):
            if not self.validate_row_col(board[row_idx]):
                return False

        # validate columns
        transposed_tuples = list(zip(*board))
        transpose_board = [list(row) for row in transposed_tuples]
        for row_idx in range(9):
            if not self.validate_row_col(transpose_board[row_idx]):
                return False
        
        # validate grid board

        row_start = 0
        row_end = 3
        col_start = 0
        col_end = 3
        combinations = []
        for i in range(0,9,3):
            for j in range(0,9,3):
                combinations.append((i, j, i+3, j+3))

        for (start_row,start_col,end_row,end_col)  in combinations:
            submatrix = self.slice_2d_matrix(
                board,
                start_row,
                end_row,
                start_col,
                end_col
            )
            if not self._validate_subboxes_of_the_grid(submatrix):
                return False
        
        return True
    def validate_row_col(self, nums: list[int]):
        # validate duplication and 1-9.
        unique_nums = []
        for num in nums:
            if num != ".":
                num = int(num)
                if num in unique_nums or num > 9 or num < 1:
                    return False
                else:
                    unique_nums.append(num)
        return True

    def _validate_subboxes_of_the_grid(self, box: list[list]):
        unique_nums = []
        for i in range(3):
            for j in range(3):
                num = box[i][j]                  
                if num != ".":
                    num = int(num)
                    if num in unique_nums or num > 9 or num < 1:
                        return False
                    else:
                        unique_nums.append(num)
        return True

    def slice_2d_matrix(self, matrix, start_row, end_row, start_col, end_col):
        """
        Slices a 2D matrix (list of lists) by specified row and column indices.
        """
        return [row[start_col:end_col] for row in matrix[start_row:end_row]]
    


        
        