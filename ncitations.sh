#!/bin/bash

DIR="$(dirname $0)"
CACHEFILE="$DIR/chache.txt"

TITLE="$(xclip -out -selection primary)"

HASH="$(echo $TITLE | md5sum | awk '{print $1}')"
NCITE="$(awk -vLOOKUPVAL=$HASH '$1 == LOOKUPVAL { print $2 }' < $CACHEFILE)"

if [ -z $NCITE ]; then
	NCITE="$(python $DIR/scholar.py -c 1 -t --phrase "$TITLE" | awk '/Citations [0-9]/ { print $2 }')"
	[ -z $NCITE ] || echo "$HASH $NCITE" >> $CACHEFILE
fi

if [ -z $NCITE ]; then
	xmessage -buttons "Ok:0" -default Ok -nearmouse "Paper not found" -timeout 5
	exit 0
fi

MESSAGE="No. citations: $NCITE"
xmessage -buttons "Ok:0,Open in browser:1" -default Ok -nearmouse "$MESSAGE" -timeout 10
RESPONSE=$?

if [ "$RESPONSE" = "1" ]; then
	sensible-browser "https://scholar.google.ch/scholar?&q=${TITLE// /+}"
fi
