#!/bin/bash
# curls to find length
curl -sLI $1 | grep -i Content-Length | awk {'print $2'}
