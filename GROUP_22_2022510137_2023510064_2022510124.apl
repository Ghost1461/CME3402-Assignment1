⎕IO ← 1

point1 ← 6 148 72 35 0 33.6 0.627 50
point2 ← 1 85 66 29 0 26.6 0.351 31

difference ← point1 - point2

sumSquares ← +/ difference * 2

distance ← sumSquares * 0.5

⎕ ← 'Euclidean Distance: '
⎕ ← distance