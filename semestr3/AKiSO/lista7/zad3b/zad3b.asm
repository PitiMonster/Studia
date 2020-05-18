section .data
    fin: db "%lf", 0
    fout: db "%lf", 10, 0

section .bss
    input resb 8

section .text
    global main
    extern printf
    extern scanf

main:
    push input
    push fin
    call scanf
    add esp, 8

    finit
    fld1
    fld qword [input]
    fld1
    fld qword [input]
    fld qword [input] ; stack = x x 1 x 1
    fmulp ; stack = x*x 1 x 1 - multiplicate st0 and st1
    faddp ; stack = x*x+1 x 1 - sum st0 and st1
    fsqrt ; stack = sqrt(x*x+1) x 1 - square root of the st0
    faddp ; stack = sqrt(x*x+1)+x 1 - sum st0 and st1
    fyl2x ; stack = 1*log2(sqrt(x*x+1)+x) - calculate st1* log2st0
    fldl2e ; stack = log2(e) log2(sqrt(x*x+1)+x) - load log2e
    fdivp ; stack =  log2(sqrt(x*x+1)+x)/log2(e) - divide st1 by st0

    fst qword [input]

    push dword [input+4]
    push dword [input]
    push fout
    call printf
    add esp, 12

    xor eax, eax
    ret