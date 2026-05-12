package main

import (
	"fmt"
	"math"
)

func main() {

	point1 := []float64{6, 148, 72, 35, 0, 33.6, 0.627, 50}
	point2 := []float64{1, 85, 66, 29, 0, 26.6, 0.351, 31}

	sumSquares := 0.0

	for i := 0; i < len(point1); i++ {
		difference := point1[i] - point2[i]
		sumSquares += difference * difference
	}

	distance := math.Sqrt(sumSquares)

	fmt.Printf("Euclidean Distance: %.3f\n", distance)
}