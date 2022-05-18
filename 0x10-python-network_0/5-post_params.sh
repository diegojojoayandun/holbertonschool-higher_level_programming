#!/bin/bash
# sends a POST request, and displays the body of the response
curl -sX POST curl -s  -X POST -F "email=hr@holbertonschool.com" -F "subject=I will always be here for PLD" "$1"
