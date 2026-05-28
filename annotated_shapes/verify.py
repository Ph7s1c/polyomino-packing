from pieces import PIECES

NAMES = ["T","P","W","V","F","U","N","Z","Y","X","L","I"]

def render(piece):
    max_col = max(c for c, r in piece)
    max_row = max(r for c, r in piece)
    return ["".join("X" if (c, r) in piece else "." for c in range(max_col + 1))
            for r in range(max_row + 1)]

for name, piece in zip(NAMES, PIECES):
    print(f"{name}")
    for row in render(piece):
        print(f"  {row}")
    print()
