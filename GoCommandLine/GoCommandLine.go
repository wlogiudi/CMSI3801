package main

import (
	"fmt"
	"math"
	"os"
	"strconv"
)

func calculatePerfectSquares(limit int) []int {
	var squares []int

	for i := 1; i <= limit; i++ {
		if math.Sqrt(float64(i)) == math.Floor(math.Sqrt(float64(i))) {
			squares = append(squares, i)
		}
	}

	return squares
}

func main() {
	if len(os.Args) < 2 {
		fmt.Println("Please provide an integer argument.")
		return
	}

	arg := os.Args[1]
	limit, err := strconv.Atoi(arg)
	if err != nil {
		fmt.Println("Please provide a valid integer argument.")
		return
	}

	if limit <= 0 {
		fmt.Println("Please provide a positive integer greater than zero.")
		return
	}

	perfectSquares := calculatePerfectSquares(limit)
	fmt.Println("Perfect squares up to", limit, "are:", perfectSquares)
}
