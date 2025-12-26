.data
A:  .word 4096
B:  .word 1
ans: .word 0

.text
.globl main

main:
    lw $t0, A
    lw $t1, B
    jal shift           #jal應該也算JUMP?
    move $v0, $t0
    sw $v0, ans
    move $a0, $v0
    li $v0, 1
    syscall
    li $v0, 10
    syscall


shift:
    div $t0, $t0, 2
    mul $t1, $t1, 2
    bne $t0, $t1, shift
    jr $ra
