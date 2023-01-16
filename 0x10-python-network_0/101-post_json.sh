#!/bin/bash
# sends a JSON POST request to url
curl -sH 'Content-Type: application/json' -d "@${2}" $@
