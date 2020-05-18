#!/bin/bash
./xasm zad8.asm
./emu6502 zad8.obx -v -m -b 1029 -e 102e
