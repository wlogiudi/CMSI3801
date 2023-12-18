package main

import "fmt"

func fibonacci() func() int {
	a, b := 0, 1
	return func() int {
		result := a
		a, b = b, a+b
		return result
	}
}

func main() {
	// Create a Fibonacci sequence generator
	fib := fibonacci()

	// Print the first 10 numbers of the Fibonacci sequence
	for i := 0; i < 10; i++ {
		fmt.Println(fib())
	}
}
