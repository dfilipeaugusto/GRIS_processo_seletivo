package main

import (
	"fmt"
	"net"
	"sync"
	"time"
)

func scan(port int, waitGroup *sync.WaitGroup, given_address string) error {
	//address := fmt.Sprintf("scanme.nmap.org:%d", port)
	address := fmt.Sprintf("%s:%d", given_address, port)
	conn, err := net.Dial("tcp", address)
	if err != nil {
		fmt.Printf("%d: %s\n", port, err.Error())
		waitGroup.Done()
		return err
	}
	conn.Close()
	fmt.Printf("%d: open\n", port)
	waitGroup.Done()
	return nil
}

func main() {
	portscanner(20, 30, "scanme.nmap.org", 2, 0)
}

func portscanner(start_port int, end_port int, given_address string, number_simultaneousCheck int, sleep_seg int) {
	var wG sync.WaitGroup

	for i:=start_port; i<=end_port; i++ {
		for j:=1; j<=number_simultaneousCheck; j++ {
			if i<=end_port {
				i++
				wG.Add(1)
				go scan(i, &wG, given_address)		
			}	
		}
		time.Sleep(time.Duration(sleep_seg)*time.Second)
	}

	wG.Wait()
}
