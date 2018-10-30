#!/bin/bash
# Shows the first and last 2 lines of a file
# First argument: file name
set -e # terminates if any error
set -u # terminates if any variable is unset
set -o pipefail # terminates if command within a 
(head -n 2; tail -n 2) < "$1"