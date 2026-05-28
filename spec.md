This project is designed to solve a Poly-omino packing problem. I have a wooden board
which has 12 pieces (all of different shapes), designed to fit into a 6 by 10 unit rectangle.

I plan on using exact_cover (Knuth's Algorithm X / Dancing Links) to find a solution
which doesn't require flipping a piece upside down (reflection).

The pieces are in order under polyomino-packing/puzzle_photos, and we will represent them
with the following data structure:

piece = {
    (0,0),
    (1,0),
    (1,1),
    (2,1),
}

Firstly, I will use computer vision (or manually annotating the images to formulate our dataset).

Then, I will create an easy way to render pieces, boards, and potential solutions 
(with colors to easily verify solutions visually).

Then, I will use exact_cover's auto-solve functionality to output a solution.
