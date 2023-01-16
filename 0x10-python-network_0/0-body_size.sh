#!/bin/bash
# takes in URL, sends a request, displays size of the body of response
curl -sI "$@" | grep -i Content-Length | awk '{print $2}'
