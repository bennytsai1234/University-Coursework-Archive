	.globl _non_reentrant_display	; 全局標記，非可重入的顯示函數
	.globl _reentrant_display	; 全局標記，可重入的顯示函數
	.globl _non_reentrant_display_PARM_2	; 全局標記，非可重入顯示函數的第二個參數
	.area OSEG	; 定義 OSEG 區域

_non_reentrant_display_PARM_2:	; 非可重入顯示函數的第二個參數區域
	.ds 1	; 定義 1 個空間
	.area CSEG  ; 定義 CSEG 區域
_non_reentrant_display:	; 非可重入的顯示函數
	mov _P1,dpl	; 將 dpl 寄存器的值移到 _P1 寄存器
	mov dptr,#_seven_segment	; 將七段顯示器數組的地址移到 dptr 寄存器
	mov a,_non_reentrant_display_PARM_2	; 將非可重入顯示函數的第二個參數移到 a 寄存器
	movc a,@a+dptr	; 從七段顯示器數組中讀取對應的模式到 a 寄存器
	mov _P2,a	; 將 a 寄存器的值移到 _P2 寄存器
	ret	; 返回
_reentrant_display:	; 可重入的顯示函數
	push _bp	; 堆棧保護
	mov _bp,sp	; 將堆棧指標移到 _bp 寄存器
	mov a,dpl	; 將 dpl 寄存器的值移到 a 寄存器
	mov _P1,a	; 將 a 寄存器的值移到 _P1 寄存器
	mov dptr,#_seven_segment	; 將七段顯示器數組的地址移到 dptr 寄存器
	mov a,_bp	; 將堆棧指標的值移到 a 寄存器
	add a,#0b11111101	; 將 a 寄存器的值增加 0b11111101
	mov r1,a	; 將 a 寄存器的值移到 r1 寄存器
	mov a,@r1	; 從堆棧中讀取值到 a 寄存器
	movc a,@a+dptr	; 從七段顯示器數組中讀取對應的模式到 a 寄存器
	mov _P2,a	; 將 a 寄存器的值移到 _P2 寄存器
	pop _bp	; 堆棧恢復
	ret	; 返回

_seven_segment:
	.db 0b00111111	; 0
	.db 0b00000110	; 1
	.db 0b01011011	; 2
	.db 0b01001111	; 3
	.db 0b01100110	; 4
	.db 0b01101101	; 5
	.db 0b01111101	; 6
	.db 0b00000111	; 7
	.db 0b01111111	; 8
	.db 0b01101111	; 9
	.db 0b01110111	; A
	.db 0b01111100	; B
	.db 0b00111001	; C
	.db 0b01011110	; D
	.db 0b01111001	; E
	.db 0b01110001	; F
	.db 0b00000000	; 