#!/bin/sh

title="$(xclip -out -selection primary)"
DIR="$(dirname $0)"
ncite="$(python $DIR/scholar.py -c 1 -t --phrase "$title" | awk '/Citations [0-9]/ { print $2 }')"

message="No. citations: $ncite"
xmessage -buttons Ok:0 -default Ok -nearmouse "$message" -timeout 10
