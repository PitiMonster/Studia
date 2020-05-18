#!/bin/bash

if(( $# != 2)); then
	echo "enter correct number of parameters"
	echo "1 - url ; 2 - duration of break"
	exit
fi

url=$1
time=$2

echo "creating folder for page history"
if [ ! -d "/home/piotrek/250125/lista4/pageHistory" ]; then
	mkdir ./pageHistory
fi
cd pageHistory

lynx -dump $url > pageContent

git init 
git add pageContent

while(sleep $time); do
	lynx -dump $url > checkedContent

	if [ -z "$( diff --brief pageContent checkedContent)" ]; then
		echo "brak zmian"
	else
		git diff
		git commit -am "zmiana"
		info=$(echo "zmiana")
		xmessage Zmiana na stronie $url
	fi

	mv checkedContent pageContent
done

