#!/bin/bash
# curls to find allowed methods
curl -sLI "$1" | grep -i Allow | awk '{$1=""; print $0}'
