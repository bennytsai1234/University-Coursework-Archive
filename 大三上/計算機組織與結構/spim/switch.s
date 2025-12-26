    .data
ans:    .word 0
cnt:    .word 6

    .text
    .globl main

main:
    li $t0, 0         
    lw $t1, cnt        
    li $t2, 0          

loop:
    bge $t0, $t1, end   # i>cnt
    rem $t3, $t0, 3     # (i%3)
    beq $t3, 0, case_0 
    beq $t3, 1, case_1 
    beq $t3, 2, case_2 

case_0:
    addi $t2, $t2, 1    
    j end_switch        

case_1:
    addi $t2, $t2, 3    
    j end_switch       

case_2:
    sub $t2, $t2, 1
    j end_switch    

end_switch:
    addi $t0, $t0, 1   
    j loop          

end:
    move $a0, $t2

    li $v0, 1
    syscall

    li $v0, 10
    syscall
