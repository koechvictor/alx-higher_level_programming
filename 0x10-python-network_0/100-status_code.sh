#!/bin/bash
# One line no pipe, redirection, ; or &&
curl -so /dev/null -Iw "%{http_code}" $@
