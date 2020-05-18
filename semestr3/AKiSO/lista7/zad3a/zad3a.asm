section .data
    formin: db "%lf", 0
    formout: db "%lf", 10, 0

section .bss
    input resb 8

section .text
    global main
    extern printf
    extern scanf

main:
    push input
    push formin
    call scanf
    add esp, 8 

    finit
    fld qword [input] ; stack = x - load x
    fldl2e ; stack = log2e x - load log2e
    fyl2x ; stack = x*log2e - multiplicate st0 and st1
    f2xm1 ; stack = 2^(x*log2e)-1 - calculate 2^(st0)-1
    fld1 ; stack = 1 2^(x*log2e)-1 - load 1
    faddp ; stack = 2^(x*log2e) - sum st1 and st0
    fld qword [input] ; stack = x 2^(x*log2e) - load x
    fchs ; stack = -x 2^(x*log2e) - reverse the sign of st0
    fldl2e ; stack = log2e -x 2^(x*log2e) load log2e
    fyl2x ; stack = -x*log2e 2^(x*log2e) - multiplicate st0 and st1
    f2xm1 ; stack = 2^(-x*log2e)-1 2^(x*log2e) - calculate 2^(st0)-1
    fld1 ; stack = 1 2^(-x*log2e)-1 2^(x*log2e) - load 1
    faddp ; stack = 2^(-x*log2e) 2^(x*log2e) - sum st0 and st1
    fsubp ; stack =  2^(-x*log2e)-2^(x*log2e) - substract st1 from st0
    fchs ; stack =  2^(x*log2e)-2^(-x*log2e) - reverse the sign of st0
    fld1 ; stack = 1 2^(x*log2e)-2^(-x*log2e) - load 1
    fld1 ; stack = 1 1 2^(x*log2e)-2^(-x*log2e) - load 1
    faddp ; stack = 2 2^(x*log2e)-2^(-x*log2e) - sum st0 and st1
    fdivp ; stack = (2^(x*log2e)-2^(-x*log2e))/2 - divide st1 by st0

    fst qword [input]

    push dword [input+4]
    push dword [input]
    push formout
    call printf
    add esp, 12

    xor eax, eax
    ret