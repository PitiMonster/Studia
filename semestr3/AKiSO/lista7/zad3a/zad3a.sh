#!/bin/bash
nasm -f elf zad3a.asm -o zad3a.o
gcc -m32 -o zad3a zad3a.o
./zad3a
