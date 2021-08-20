#!/bin/bash
# Bash script that takes all HTTP methods the server will accept.
curl -sI "$1" | grep "Allow" | cut -d " " -f2-
