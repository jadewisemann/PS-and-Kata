"""
problem: '혼자서 하느 틱택토'
tags: ¿단순구현? 
difficulty: LV2
source: programmers
link: https://school.programmers.co.kr/learn/courses/30/lessons/160585
"""

CIRCLE = "O"
CROSS = "X"
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
    
    o_count = ''.join(board).count(CIRCLE)
    x_count = ''.join(board).count(CROSS)
    
    if not (o_count == x_count or o_count == x_count + 1):
        return 0

    o_win = check_win(board, CIRCLE)
    x_win = check_win(board, CROSS)
    
    # 선공이 이겼는데
    if o_win and (  
        x_win  # 후공도 이길수는 없다
        or o_count == x_count  # 후공의 말이 선공과 같을 수는 없다
        or not o_count == x_count + 1  # 후공의 말이 선공의 말보다 하나 초과하여, 작을 수 없다.
    ): return 0


    if x_win and not (o_count == x_count):  
        return 0
    
    return 1