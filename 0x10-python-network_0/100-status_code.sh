#!/bin/bash
# Only status code
curl -sIw %{http_code} $1 -o /dev/null
