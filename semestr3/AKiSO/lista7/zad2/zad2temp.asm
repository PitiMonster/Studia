section .bss
digit resb 1
bufer resb 10

section .text
global _start

_start:
	call _printQuestion			; wypisanie pytania o liczbę
	call _readN					; wczytanie N
	lea esi, [N] 					; rzucenie na esi adresu N
	call string_to_int 			; zamiana N na int
	mov [N], eax 						; przniesienie na N jego wartośc jako int
	mov [tempN], dword 1			; wpisanie 1 pod obie wartości zmiennych
	mov [tempNumber], dword 1
	
	call _printNumber
	
_printQuestion:
	mov eax, 4
	mov ebx, 1	; plik do którego wypiszemy 1 - konsola
	mov ecx, question	; co wypiszemy
	mov edx, questionLength ; dlugosc wypisanego tekstu
	int 80h		; przerwanie 
	ret	; powrót

_readN:
	mov eax, 3		; eax = 3 syscall read
	xor ebx,ebx
	mov ecx, N
	mov edx, 10
	int 80h
	ret
	
_printNumber:	
	mov eax, [tempNumber]
	cmp eax, [tempN]
	jg _nextValue
	call _clearBuffer
	mov esi, bufer
	mov eax, [tempNumber]
	call int_to_string
	mov ecx, eax
	mov eax, 4
	mov ebx, 1
	mov edx, 10
	int 80h
	
	call _printSpace
	
	mov eax, [tempNumber]		; set tempNumber += 1
	inc eax
	mov [tempNumber], eax
	
	call _printNumber
	

_nextValue:
	call _printNewLine
	mov eax, [tempN] ; increment tempN value
	inc eax
	mov [tempN], eax
	cmp eax, [N]
	jg _exit	; if tempN > N exit program
	xor eax, eax
	inc eax
	mov [tempNumber], eax ; else printNumber again
	jmp _printNumber
	
_printSpace:
	mov eax, 4
  mov ebx, 1
  mov ecx, space
  mov edx, 1
  int 80h
  ret
  
_printNewLine:
	mov eax, 4
  mov ebx, 1
  mov ecx, newLineMsg
  mov edx, newLineLen
  int 80h
  ret
	
; Input:
; ESI = pointer to the string to convert
; ECX = number of digits in the string (must be > 0)
; Output:
; EAX = integer value
string_to_int:
  xor ebx,ebx    ; clear ebx
.next_digit:
  movzx eax,byte[esi]
  inc esi
  cmp eax, '0'
  jl .done
  cmp eax, '9'
  jg .done
  sub al,'0'    ; convert from ASCII to number
  imul ebx,10
  add ebx,eax   ; ebx = ebx*10 + eax
  call .next_digit  ; while (--ecx)
.done:
	mov eax, ebx
  ret

; Input:
; EAX = integer value to convert
; ESI = pointer to buffer to store the string in (must have room for at least 10 bytes)
; Output:
; EAX = pointer to the first character of the generated string
int_to_string:
  add esi,9
  mov byte [esi],STRING_TERMINATOR
  dec esi

  mov ebx,10         
.next_digit:
  xor edx,edx         ; Clear edx prior to dividing edx:eax by ebx
  div ebx             ; eax /= 10
  add dl,'0'          ; Convert the remainder to ASCII 
  mov [esi],dl
  dec esi             ; store characters in reverse order
  
  test eax,eax            
  jnz .next_digit     ; Repeat until eax==0
  ;mov eax, 4
  ;mov ebx, 1
  ;mov ecx, esi
  ;mov edx,10
  ;int 80h
  mov eax,esi
  ret


_clearBuffer:				; clear bufer
	lea esi, [bufer]
	mov ecx, 10			; ecx equals 10 to loop 10 times
.nextClear:
	mov byte[esi], 0
	inc esi
	loop .nextClear
	ret

_exit:
	mov eax, 1
	xor ebx, ebx
	int 80h

section .data

new_line db 10,13
space db " ", 0ah
newLineMsg db 0xA, 0xD
newLineLen equ $-newLineMsg
question db "Provide number:", 0ah
questionLength equ $ - question
tempN times 10 db 0
tempNumber times 10 db 0
N times 10 db 0
tempString times 10 db 0
STRING_TERMINATOR equ 0

