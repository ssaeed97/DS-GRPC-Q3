package main

import (
    "bufio"
    "fmt"
    "net"
    "os"
)

const (
    SERVER_HOST = "127.0.0.1"
    SERVER_PORT = "5002"
    SERVER_TYPE = "tcp"
)

func main() {
    connection, err := net.Dial(SERVER_TYPE, SERVER_HOST+":"+SERVER_PORT)
    if err != nil {
        fmt.Println("Error connecting:", err.Error())
        return
    }
    defer connection.Close()

    go readServerMessages(connection)

    scanner := bufio.NewScanner(os.Stdin)
    fmt.Print("Enter username: ")
    scanner.Scan()
    username := scanner.Text()

    for {
        fmt.Print("> ")
        scanner.Scan()
        msg := scanner.Text()
        _, err := connection.Write([]byte(username + "<SEP>" + msg + "\n"))
        if err != nil {
            fmt.Println("Error sending:", err.Error())
            break
        }
    }
}

func readServerMessages(conn net.Conn) {
    scanner := bufio.NewScanner(conn)
    for scanner.Scan() {
        fmt.Println("\n" + scanner.Text())
        fmt.Print("> ")
    }
}