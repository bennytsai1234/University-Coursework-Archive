li $t0, 0
li $t1, 0
move $s3, $s0
move $s4, $s1

# 假設 D 的基地址已經存在於 $s2 中

mul $t2, $t1, 4

loop_i:
  bge $t0, $s3, end_loop_i
  li $t1, 0

  loop_j:
    bge $t1, $s4, end_loop_j
    add $t3, $s2, $t2
    add $t4, $t0, $t1
    sw $t4, 0($t3)
    addi $t1, $t1, 1
    j loop_j

  end_loop_j:
    addi $t0, $t0, 1
    j loop_i

end_loop_i:
