"""
Generates a complete minesweeper board.
"""

import numpy as np
import random
import functools
import re

def minesweeper_board(size, mines):
    """
    Generates a 2-tuple of (is it a mine?, # of neighbour or self mines).
    Both are 2d arrays.
    If the tile is a mine, ignore the second value.
    """
    is_mine = np.zeros((size[0]+2,size[1]+2),dtype=int)
    for raw in random.sample(range(size[0]*size[1]),mines):
        x,y=divmod(raw,size[1])
        is_mine[x+1,y+1]=1
    around = np.array(is_mine)
    around = around[0:size[0],:]+around[1:size[0]+1,:]+around[2:size[0]+2,:]
    around = around[:,0:size[1]]+around[:,1:size[1]+1]+around[:,2:size[1]+2]
    is_mine = is_mine[1:size[0]+1,1:size[1]+1]
    return is_mine, around

def minesweeper_board_clear(size, mines, clear=0):
    """
    Generates a raw board.
    Require a certain size square in the top left to be clear.
    """
    is_mine, around = minesweeper_board(size, mines)
    while not np.all(around[0:clear,0:clear]==0):
        is_mine, around = minesweeper_board(size, mines)
    return is_mine, around

def minesweeper_board_simple(size, mines, *args, **kwargs):
    """
    Generates a simple text board.
    """
    is_mine, around = minesweeper_board_clear(size, mines, *args, **kwargs)
    texts = np.where(is_mine, 'X', np.choose(around, '+123456789'))
    return '\n'.join(map(''.join,texts))

def minesweeper_board_discord(size, mines, *args, **kwargs):
    """
    Generates a simple text board.
    """
    raw = minesweeper_board_simple(size, mines, *args, **kwargs)
    return re.sub('([^\\s])','||`\\1`||',raw)