#!/bin/bash

str=$(curl --request GET   --url 'https://api.thecatapi.com/v1/images/search?mime_types=jpg&format=json'   --header 'x-api-key: 70404b1b-2e44-408e-8d90-c0c4a3a6f6dd' | jq -r '.[0].url')
wget -O kot.jpg $str
img2txt -f utf8 -W 150 "kot.jpg"
rm kot.jpg
curl -get http://api.icndb.com/jokes/random/ | jq '.value.joke'
