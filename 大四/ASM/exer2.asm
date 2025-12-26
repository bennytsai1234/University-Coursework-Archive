test     start   1000 
loop1    rd      char 
         lda     index1
         comp    char
         jgt     output
         comp    char
         jlt     loop2
loop2    lda     index2
         comp    char
         jgt     chg1
         comp    char
         jlt     loop3
loop3    lda     index3
         comp    char
         jgt     output
         comp    char
         jlt     loop4
loop4    lda     index4
         comp    char
         jgt     chg2
         comp    char
         jlt     output
chg1     lda     index5
         add     char
         sta     char
         j       output
chg2     lda     index5
         sub     char
         sta     char
         j       output
output   wd      char
         j       loop1
char     byte    c'A'
input    byte    c'A'
index1   byte    c'A'
index2   byte    c'Z'
index3   byte    c'a'
index4   byte    c'z'
index5   byte    x'20'
