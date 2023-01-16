#!/bin/bash
# Send GET request to URL and siplays the content of the response
curl -sd "email=test@gmail.com" -d "subject=I will always be here for PLD" $@
