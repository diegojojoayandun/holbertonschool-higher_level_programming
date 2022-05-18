#!/bin/bash
# sends a POST request, and displays the body of the response
curl -s "$1" -X POST -F "email=hr@holbertonschool.com" -F "subject=I will always be here for PLD"
