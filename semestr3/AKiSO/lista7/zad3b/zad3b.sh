#!/bin/bash
nasm -f elf zad3b.asm -o zad3b.o
gcc -m32 -o zad3b zad3b.o
./zad3b
