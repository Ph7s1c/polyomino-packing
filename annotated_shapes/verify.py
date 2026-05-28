"""Print an ASCII grid for each piece so shapes can be checked against the photos."""
from pieces import PIECES

NAMES = ["T","P","W","V","F","U","N","Z","Y","X","L","I"]

def render(piece):
    max_col = max(c for c, r in piece)
    max_row = max(r for c, r in piece)
    rows = []
    for r in range(max_row + 1):
        rows.append("".join("X" if (c, r) in piece else "." for c in range(max_col + 1)))
    return rows

for i, (piece, name) in enumerate(zip(PIECES, NAMES), 1):
    print(f"Piece {i:>2} ({name})  — photo {i}.jpeg")
    for row in render(piece):
        print(f"  {row}")
    print()
