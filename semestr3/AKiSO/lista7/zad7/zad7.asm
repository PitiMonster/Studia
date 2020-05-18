section .bss
    input resd 1
    res resb 16

section .data
	formin: db "%d", 0
	formout: db "The result is = %08x%08x%08x%08x", 10, 0

section .text
	global  main
        extern  printf
	extern scanf
main:
	push	ebp
	mov	ebp, esp

	push input
  	push formin
  	call scanf
	mov ecx , dword [input]	; ecx = input

	mov dword[ebp - 16], 1	; te 4 linjki wrzucją nam jedynki do rejestrów
	movd xmm2, [ebp - 16]
	movd xmm0, [ebp - 16]
	movd xmm1, [ebp - 16]
	
l1:
	movaps xmm7, xmm0 
	
	pmuludq xmm7, xmm1		

	movaps xmm3,xmm0
	PSRLDQ  xmm3, 0x04
	pmuludq xmm3, xmm1
	PSLLDQ  xmm3, 0x04
	paddq xmm7, xmm3
	
	movaps xmm3,xmm0
	PSRLDQ  xmm3, 0x08
	pmuludq xmm3, xmm1
	PSLLDQ  xmm3, 0x08
	paddq xmm7, xmm3
	
	movaps xmm3,xmm0
	PSRLDQ  xmm3, 0x0c
	pmuludq xmm3, xmm1
	PSLLDQ  xmm3, 0x0c
	paddq xmm7, xmm3

	movaps xmm0, xmm7
	paddq xmm1, xmm2
	
	pextrw eax,xmm7,0
	loop l1

	pextrd [res], xmm0, 0
    	pextrd [res+4], xmm0, 1
	pextrd [res+8], xmm0, 2
    	pextrd [res+12], xmm0, 3
	push dword [res]
    	push dword [res+4]
    	push dword [res+8]
    	push dword [res+12]
	push formout
	call printf

	leave
	ret
A:	dq 0
	dq 1
	dq 2
	dq 3
