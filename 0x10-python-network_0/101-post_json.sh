#!/bin/bash
# cURL a JSON file
curl -sX POST "$1" -H 'Content-Type: application/json' -d @"$2"
