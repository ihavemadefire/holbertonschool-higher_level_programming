#!bin/bash/
# return just the http code
curl -s -o /dev/null -I -w "%{http_code}" "$1"
