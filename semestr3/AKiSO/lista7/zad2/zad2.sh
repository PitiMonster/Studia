#!/bin/bash
nasm -f elf zad2temp.asm -o zad2.o
ld -m elf_i386 -o zad2 zad2.o

