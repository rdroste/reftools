#!/bin/bash

title="$(xclip -out -selection primary)"
DIR="$(dirname $0)"
ncite="$(python $DIR/scholar.py -c 1 -t --phrase "$title" | awk '/Citations [0-9]/ { print $2 }')"

if [ -z $ncite ]; then
	xmessage -buttons "Ok:0" -default Ok -nearmouse "Paper not found" -timeout 5
	exit 0
fi

message="No. citations: $ncite"
xmessage -buttons "Ok:0,Open in browser:1" -default Ok -nearmouse "$message" -timeout 10
response=$?

if [ "$response" = "1" ]; then
	sensible-browser "https://scholar.google.ch/scholar?&q=${title// /+}"
fi
