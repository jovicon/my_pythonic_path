'''
number: 27 
name: Valid Sudoku  
dificulty: Medium 
url: https://leetcode.com/problems/valid-sudoku/

Determine if a 9x9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:

Each row must contain the digits 1-9 without repetition.
Each column must contain the digits 1-9 without repetition.
Each of the 9 3x3 sub-boxes of the grid must contain the digits 1-9 without repetition.

A partially filled sudoku which is valid.

The Sudoku board could be partially filled, where empty cells are filled with the character '.'.

Example 1:

Input:
[
  ["5","3",".",".","7",".",".",".","."],
  ["6",".",".","1","9","5",".",".","."],
  [".","9","8",".",".",".",".","6","."],
  ["8",".",".",".","6",".",".",".","3"],
  ["4",".",".","8",".","3",".",".","1"],
  ["7",".",".",".","2",".",".",".","6"],
  [".","6",".",".",".",".","2","8","."],
  [".",".",".","4","1","9",".",".","5"],
  [".",".",".",".","8",".",".","7","9"]
]
Output: true


Example 2:
Input:
[
  ["8","3",".",".","7",".",".",".","."],
  ["6",".",".","1","9","5",".",".","."],
  [".","9","8",".",".",".",".","6","."],
  ["8",".",".",".","6",".",".",".","3"],
  ["4",".",".","8",".","3",".",".","1"],
  ["7",".",".",".","2",".",".",".","6"],
  [".","6",".",".",".",".","2","8","."],
  [".",".",".","4","1","9",".",".","5"],
  [".",".",".",".","8",".",".","7","9"]
]
Output: false

Explanation: Same as Example 1, except with the 5 in the top left corner being 
    modified to 8. Since there are two 8's in the top left 3x3 sub-box, it is invalid.

Note:
    A Sudoku board (partially filled) could be valid but is not necessarily solvable.
    Only the filled cells need to be validated according to the mentioned rules.
    The given board contain only digits 1-9 and the character '.'.
    The given board size is always 9x9.
'''

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        validate = True 
        
        hash_row = []
        hash_columns = []
        # row validation -- done
        for i,row in enumerate(board):
            
                    
            for j,str_number_row in enumerate(row):

                if str_number_row in hash_row:
                    return False
                elif str_number_row != '.':
                    hash_row.append(str_number_row)
                
            hash_row = []
        
            
        i = 0
        j = 0
        # column validation -- done
        while i < 9:
            while j < 9:
                if board[j][i] in hash_columns:
                    return False
                elif board[j][i] != '.':
                    hash_columns.append(board[j][i])
                j += 1
                
            hash_columns = []    
            i += 1
            j = 0
            
        
        # 3x3 validation
        validate = self.isValid3x3(board[:3]) and self.isValid3x3(board[3:6]) and self.isValid3x3(board[6:])
        
        return validate
    
    
    def isValid3x3(self,board: List[List[str]])-> bool:
        
        i = 0
        j = 0
        hash_columns = []
        while i < 9:
            if i == 3 or i == 6:
                hash_columns = []
            
            while j < 3:
                if board[j][i] in hash_columns:
                    return False
                elif board[j][i] != '.':
                    hash_columns.append(board[j][i])
            
                j += 1
            
            i += 1
            j = 0
        
        return True