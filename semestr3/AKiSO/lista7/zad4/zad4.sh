#!bin/bash
nasm -o zad4 zad4.asm
qemu-system-i386  -fda zad4 -net none
