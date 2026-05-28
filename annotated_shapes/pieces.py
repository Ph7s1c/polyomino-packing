# Coordinates are (col, row) with (0, 0) at top-left, col increases right, row increases down.
# Each piece is shown placed in the top-left corner of the board (as in the source photos).
# Some identifications (marked ?) are uncertain and should be verified against the photos.

# Photo 1 — T-pentomino
# X X X
#   X
#   X
piece_1 = {(0,0),(1,0),(2,0),(1,1),(1,2)}

# Photo 2 — P-pentomino  (?)
# X
# X X
# X X
piece_2 = {(0,0),(0,1),(1,1),(0,2),(1,2)}

# Photo 3 — W-pentomino  (?)
# X
# X X
#   X X
piece_3 = {(0,0),(0,1),(1,1),(1,2),(2,2)}

# Photo 4 — V-pentomino
# X X X
# X
# X
piece_4 = {(0,0),(1,0),(2,0),(0,1),(0,2)}

# Photo 5 — F-pentomino  (?)
#   X X
# X X
#   X
piece_5 = {(1,0),(2,0),(0,1),(1,1),(1,2)}

# Photo 6 — U-pentomino  (?)
# X   X
# X X X
piece_6 = {(0,0),(2,0),(0,1),(1,1),(2,1)}

# Photo 7 — N-pentomino  (?)
# X
# X X
#   X
#   X
piece_7 = {(0,0),(0,1),(1,1),(1,2),(1,3)}

# Photo 8 — Z-pentomino  (?)
# X X
#   X
#   X X
piece_8 = {(0,0),(1,0),(1,1),(1,2),(2,2)}

# Photo 9 — Y-pentomino  (?)
#   X
# X X
#   X
#   X
piece_9 = {(1,0),(0,1),(1,1),(1,2),(1,3)}

# Photo 10 — X-pentomino
#   X
# X X X
#   X
piece_10 = {(1,0),(0,1),(1,1),(2,1),(1,2)}

# Photo 11 — L-pentomino (mirrored / J-orientation)  (?)
#   X
#   X
#   X
# X X
piece_11 = {(1,0),(1,1),(1,2),(0,3),(1,3)}

# Photo 12 — I-pentomino
# X X X X X
piece_12 = {(0,0),(1,0),(2,0),(3,0),(4,0)}

PIECES = [
    piece_1,
    piece_2,
    piece_3,
    piece_4,
    piece_5,
    piece_6,
    piece_7,
    piece_8,
    piece_9,
    piece_10,
    piece_11,
    piece_12,
]
