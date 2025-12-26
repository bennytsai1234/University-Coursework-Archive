.data
A: .word 1, 2, 4, 6, 8  
Target: .word 5           

.text
.globl main
main:
    la $s0, A            
    lw $s1, Target       
    li $t3, 0            

    loop_outer:
        lw $t0, 0($s0)  
        la $s2, A         
        li $t4, 0         

        loop_inner:
            lw $t1, 0($s2)  
            add $t2, $t0, $t1  

            beq $t0, $t1, not_equal  
            beq $t2, $s1, found  

            not_equal:
            addi $s2, $s2, 4  
            addi $t4, $t4, 1   
            bnez $t1, loop_inner  

        addi $s0, $s0, 4
        addi $t3, $t3, 1   
        bnez $t0, loop_outer  

    found:
        move $a0, $t3  
        li $v0, 1      
        syscall

        li $v0, 11     
        li $a0, ' '    
        syscall

        move $a0, $t4  
        li $v0, 1      
        syscall

        li $v0, 10    
        syscall
