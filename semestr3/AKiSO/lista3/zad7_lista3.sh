#!/bin/bash

for plik in ./*; do
	if [[ -f $plik ]]; then 
		mv "$plik" "${plik,,}"
	fi
done
