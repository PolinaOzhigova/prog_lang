%macro DoPrint 2
        movsd xmm0, qword %1
        mov  rdi, %2
        mov  eax, 1
        call printf
%endmacro

global main
default rel
extern printf

section .text
main:
        sub  rsp, 8

        fld qword [num]
        fsqrt
        fst qword [result]

        DoPrint [num], ms1
        DoPrint [result], ms2

        add  rsp, 8
        xor  eax, eax
        ret

section .data
        ms1 db `\nКорень из %f `, 0
        ms2 db `равен %f\n\n`, 0
        num dq 25.0
        result dq 0.0