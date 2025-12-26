.data
A: .float 1.0  
B: .float 2.0
ans: .float 0.0

.text
.globl main
main:
    lwc1 $f0, A
    lwc1 $f1, B

    li.s $f2, 6.0
    mul.s $f0, $f0, $f2

    li.s $f3, 8.0
    add.s $f0, $f0, $f3

    li.s $f4, 2.0
    div.s $f1, $f1, $f4

    mul.s $f5, $f0, $f1

    mov.s $f12, $f5
    li $v0, 2
    syscall

    li $v0, 10
    syscall
