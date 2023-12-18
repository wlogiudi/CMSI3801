package main

import (
	"fmt"
	"io"
	"net/http"
	"os"
	"sync"
)

func fetchURL(url string, wg *sync.WaitGroup, ch chan string) {
	defer wg.Done()

	resp, err := http.Get(url)
	if err != nil {
		fmt.Printf("Error fetching %s: %s\n", url, err)
		return
	}
	defer resp.Body.Close()

	if resp.StatusCode != http.StatusOK {
		fmt.Printf("Error: %s returned status %s\n", url, resp.Status)
		return
	}

	filename := fmt.Sprintf("%s.html", url) // Naming file after URL
	file, err := os.Create(filename)
	if err != nil {
		fmt.Printf("Error creating file for %s: %s\n", url, err)
		return
	}
	defer file.Close()

	_, err = io.Copy(file, resp.Body)
	if err != nil {
		fmt.Printf("Error writing response for %s: %s\n", url, err)
		return
	}

	ch <- url // Send a message to the channel indicating completion
}

func main() {
	urls := []string{
		"https://example.com",
		"https://www.google.com",
		"https://www.wikipedia.org",
		// Add more URLs to download concurrently
	}

	var wg sync.WaitGroup
	ch := make(chan string)

	for _, url := range urls {
		wg.Add(1)
		go fetchURL(url, &wg, ch)
	}

	go func() {
		wg.Wait()
		close(ch) // Close the channel after all goroutines finish
	}()

	// Receive messages from the channel to know when downloads are complete
	for completedURL := range ch {
		fmt.Printf("Downloaded: %s\n", completedURL)
	}
}
