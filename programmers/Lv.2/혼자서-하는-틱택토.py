"""
problem: '혼자서 하는 틱택토'
tags: ¿단순구현? 
difficulty: LV2
source: programmers
link: https://school.programmers.co.kr/learn/courses/30/lessons/160585
"""

FIRST_PLAYER = "O"
SECOND_PLAYER = "X"
BOARD_SIZE = 3

def check_win(board, player):

    for i in range(len(board)):
        if (
            all(board[i][j] == player for j in range(BOARD_SIZE)) 
            or all(board[j][i] == player for j in range(BOARD_SIZE))
        ): return True
    
    if (
        all ([board[i][i] == player for i in range(BOARD_SIZE)]) 
        or all ([board[i][BOARD_SIZE-1-i] == player for i in range(BOARD_SIZE)])
    ): return True
    
    return False

def solution(board):
    
    first_marker_counter = ''.join(board).count(FIRST_PLAYER)
    second_marker_counter = ''.join(board).count(SECOND_PLAYER)
    
    if not (
        first_marker_counter == second_marker_counter 
        or first_marker_counter == second_marker_counter + 1
    ):return 0

    is_first_win = check_win(board, FIRST_PLAYER)
    is_second_win = check_win(board, SECOND_PLAYER)
    
    if is_first_win and (  
        is_second_win 
        or first_marker_counter == second_marker_counter 
        or not first_marker_counter -1 == second_marker_counter
    ): return 0


    if is_second_win and not (first_marker_counter == second_marker_counter):  
        return 0
    
    return 1