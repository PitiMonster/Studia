#!/bin/bash
nasm -f elf zad7.asm -o zad7.o
gcc -m32 -o zad7 zad7.o
./zad7
