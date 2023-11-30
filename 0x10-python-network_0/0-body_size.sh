#!/bin/bash
# send a request to an URL with curl, and displays the size of the body of the response
# Check if URL is provided
if [ -z "$1" ]; then
    echo "Usage: $0 <URL>"
    exit 1
fi
curl -sI "$1" | grep -i "Content-Length" | awk '{print $2}'
