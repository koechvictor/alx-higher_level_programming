#!/bin/bash
# uses curl to display all HTTP methods server will accept
curl -sI "$@" | grep -i Allow | cut -d ' ' -f 2-
