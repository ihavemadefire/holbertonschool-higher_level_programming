#!/bin/bash
# curls to find allowed methods
curl -sLI "$1" | grep -i Allow | cut -d " " -f 2-
