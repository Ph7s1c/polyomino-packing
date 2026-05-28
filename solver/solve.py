import sys, os
import numpy as np

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from annotated_shapes.pieces import PIECES
from exact_cover import get_exact_cover

COLS, ROWS = 6, 10
NAMES = list("TPWVFUNZYXLI")

COLORS = [
    '\033[41m', '\033[42m', '\033[43m', '\033[44m',
    '\033[45m', '\033[46m', '\033[101m', '\033[102m',
    '\033[103m', '\033[104m', '\033[105m', '\033[106m',
]
RESET = '\033[0m'


def normalize(cells):
    mc, mr = min(c for c, r in cells), min(r for c, r in cells)
    return frozenset((c - mc, r - mr) for c, r in cells)

def rotate90(cells):
    return normalize(frozenset((r, -c) for c, r in cells))

def rotations(piece):
    seen, result, p = set(), [], normalize(frozenset(piece))
    for _ in range(4):
        if p not in seen:
            seen.add(p)
            result.append(p)
        p = rotate90(p)
    return result

def placements(piece):
    result = []
    for rot in rotations(piece):
        max_c = max(c for c, r in rot)
        max_r = max(r for c, r in rot)
        for dc in range(COLS - max_c):
            for dr in range(ROWS - max_r):
                result.append(frozenset((c + dc, r + dr) for c, r in rot))
    return result


options = [(i, p) for i, piece in enumerate(PIECES) for p in placements(piece)]

matrix = np.zeros((len(options), len(PIECES) + COLS * ROWS), dtype=np.uint8)
for idx, (pi, cells) in enumerate(options):
    matrix[idx, pi] = 1
    for c, r in cells:
        matrix[idx, len(PIECES) + r * COLS + c] = 1

solution = get_exact_cover(matrix)

board = [[-1] * COLS for _ in range(ROWS)]
for idx in solution:
    pi, cells = options[idx]
    for c, r in cells:
        board[r][c] = pi

for row in board:
    print(''.join(f"{COLORS[pi]}{NAMES[pi]}{RESET}" for pi in row))
