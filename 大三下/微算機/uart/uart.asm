;--------------------------------------------------------
; File Created by SDCC : free open source ISO C Compiler 
; Version 4.4.0 #14620 (MINGW64)
;--------------------------------------------------------
	.module uart
	.optsdcc -mmcs51 --model-small
	
;--------------------------------------------------------
; Public variables in this module
;--------------------------------------------------------
	.globl _updateDigits_PARM_3
	.globl _updateDigits_PARM_2
	.globl _displayDigit_PARM_2
	.globl _main
	.globl _uart_isr
	.globl _reset
	.globl _UART_init
	.globl _Timer0_ISR
	.globl _updateDigits
	.globl _KeyScan
	.globl _txsend
	.globl _send
	.globl _displayDigit
	.globl _TF2
	.globl _EXF2
	.globl _RCLK
	.globl _TCLK
	.globl _EXEN2
	.globl _TR2
	.globl _C_T2
	.globl _CP_RL2
	.globl _T2CON_7
	.globl _T2CON_6
	.globl _T2CON_5
	.globl _T2CON_4
	.globl _T2CON_3
	.globl _T2CON_2
	.globl _T2CON_1
	.globl _T2CON_0
	.globl _PT2
	.globl _ET2
	.globl _CY
	.globl _AC
	.globl _F0
	.globl _RS1
	.globl _RS0
	.globl _OV
	.globl _F1
	.globl _P
	.globl _PS
	.globl _PT1
	.globl _PX1
	.globl _PT0
	.globl _PX0
	.globl _RD
	.globl _WR
	.globl _T1
	.globl _T0
	.globl _INT1
	.globl _INT0
	.globl _TXD
	.globl _RXD
	.globl _P3_7
	.globl _P3_6
	.globl _P3_5
	.globl _P3_4
	.globl _P3_3
	.globl _P3_2
	.globl _P3_1
	.globl _P3_0
	.globl _EA
	.globl _ES
	.globl _ET1
	.globl _EX1
	.globl _ET0
	.globl _EX0
	.globl _P2_7
	.globl _P2_6
	.globl _P2_5
	.globl _P2_4
	.globl _P2_3
	.globl _P2_2
	.globl _P2_1
	.globl _P2_0
	.globl _SM0
	.globl _SM1
	.globl _SM2
	.globl _REN
	.globl _TB8
	.globl _RB8
	.globl _TI
	.globl _RI
	.globl _P1_7
	.globl _P1_6
	.globl _P1_5
	.globl _P1_4
	.globl _P1_3
	.globl _P1_2
	.globl _P1_1
	.globl _P1_0
	.globl _TF1
	.globl _TR1
	.globl _TF0
	.globl _TR0
	.globl _IE1
	.globl _IT1
	.globl _IE0
	.globl _IT0
	.globl _P0_7
	.globl _P0_6
	.globl _P0_5
	.globl _P0_4
	.globl _P0_3
	.globl _P0_2
	.globl _P0_1
	.globl _P0_0
	.globl _TH2
	.globl _TL2
	.globl _RCAP2H
	.globl _RCAP2L
	.globl _T2CON
	.globl _B
	.globl _ACC
	.globl _PSW
	.globl _IP
	.globl _P3
	.globl _IE
	.globl _P2
	.globl _SBUF
	.globl _SCON
	.globl _P1
	.globl _TH1
	.globl _TH0
	.globl _TL1
	.globl _TL0
	.globl _TMOD
	.globl _TCON
	.globl _PCON
	.globl _DPH
	.globl _DPL
	.globl _SP
	.globl _P0
	.globl _arr
	.globl _Digits
	.globl _BB
	.globl _AA
	.globl _seg
	.globl _idx
	.globl _pos
	.globl _rx_data
	.globl _tx_data
	.globl _gx_data
	.globl _random_num
	.globl _zero_duration
	.globl _previousksr
	.globl _ksr
	.globl _cnt
;--------------------------------------------------------
; special function registers
;--------------------------------------------------------
	.area RSEG    (ABS,DATA)
	.org 0x0000
_P0	=	0x0080
_SP	=	0x0081
_DPL	=	0x0082
_DPH	=	0x0083
_PCON	=	0x0087
_TCON	=	0x0088
_TMOD	=	0x0089
_TL0	=	0x008a
_TL1	=	0x008b
_TH0	=	0x008c
_TH1	=	0x008d
_P1	=	0x0090
_SCON	=	0x0098
_SBUF	=	0x0099
_P2	=	0x00a0
_IE	=	0x00a8
_P3	=	0x00b0
_IP	=	0x00b8
_PSW	=	0x00d0
_ACC	=	0x00e0
_B	=	0x00f0
_T2CON	=	0x00c8
_RCAP2L	=	0x00ca
_RCAP2H	=	0x00cb
_TL2	=	0x00cc
_TH2	=	0x00cd
;--------------------------------------------------------
; special function bits
;--------------------------------------------------------
	.area RSEG    (ABS,DATA)
	.org 0x0000
_P0_0	=	0x0080
_P0_1	=	0x0081
_P0_2	=	0x0082
_P0_3	=	0x0083
_P0_4	=	0x0084
_P0_5	=	0x0085
_P0_6	=	0x0086
_P0_7	=	0x0087
_IT0	=	0x0088
_IE0	=	0x0089
_IT1	=	0x008a
_IE1	=	0x008b
_TR0	=	0x008c
_TF0	=	0x008d
_TR1	=	0x008e
_TF1	=	0x008f
_P1_0	=	0x0090
_P1_1	=	0x0091
_P1_2	=	0x0092
_P1_3	=	0x0093
_P1_4	=	0x0094
_P1_5	=	0x0095
_P1_6	=	0x0096
_P1_7	=	0x0097
_RI	=	0x0098
_TI	=	0x0099
_RB8	=	0x009a
_TB8	=	0x009b
_REN	=	0x009c
_SM2	=	0x009d
_SM1	=	0x009e
_SM0	=	0x009f
_P2_0	=	0x00a0
_P2_1	=	0x00a1
_P2_2	=	0x00a2
_P2_3	=	0x00a3
_P2_4	=	0x00a4
_P2_5	=	0x00a5
_P2_6	=	0x00a6
_P2_7	=	0x00a7
_EX0	=	0x00a8
_ET0	=	0x00a9
_EX1	=	0x00aa
_ET1	=	0x00ab
_ES	=	0x00ac
_EA	=	0x00af
_P3_0	=	0x00b0
_P3_1	=	0x00b1
_P3_2	=	0x00b2
_P3_3	=	0x00b3
_P3_4	=	0x00b4
_P3_5	=	0x00b5
_P3_6	=	0x00b6
_P3_7	=	0x00b7
_RXD	=	0x00b0
_TXD	=	0x00b1
_INT0	=	0x00b2
_INT1	=	0x00b3
_T0	=	0x00b4
_T1	=	0x00b5
_WR	=	0x00b6
_RD	=	0x00b7
_PX0	=	0x00b8
_PT0	=	0x00b9
_PX1	=	0x00ba
_PT1	=	0x00bb
_PS	=	0x00bc
_P	=	0x00d0
_F1	=	0x00d1
_OV	=	0x00d2
_RS0	=	0x00d3
_RS1	=	0x00d4
_F0	=	0x00d5
_AC	=	0x00d6
_CY	=	0x00d7
_ET2	=	0x00ad
_PT2	=	0x00bd
_T2CON_0	=	0x00c8
_T2CON_1	=	0x00c9
_T2CON_2	=	0x00ca
_T2CON_3	=	0x00cb
_T2CON_4	=	0x00cc
_T2CON_5	=	0x00cd
_T2CON_6	=	0x00ce
_T2CON_7	=	0x00cf
_CP_RL2	=	0x00c8
_C_T2	=	0x00c9
_TR2	=	0x00ca
_EXEN2	=	0x00cb
_TCLK	=	0x00cc
_RCLK	=	0x00cd
_EXF2	=	0x00ce
_TF2	=	0x00cf
;--------------------------------------------------------
; overlayable register banks
;--------------------------------------------------------
	.area REG_BANK_0	(REL,OVR,DATA)
	.ds 8
	.area REG_BANK_1	(REL,OVR,DATA)
	.ds 8
	.area REG_BANK_3	(REL,OVR,DATA)
	.ds 8
;--------------------------------------------------------
; overlayable bit register bank
;--------------------------------------------------------
	.area BIT_BANK	(REL,OVR,DATA)
bits:
	.ds 1
	b0 = bits[0]
	b1 = bits[1]
	b2 = bits[2]
	b3 = bits[3]
	b4 = bits[4]
	b5 = bits[5]
	b6 = bits[6]
	b7 = bits[7]
;--------------------------------------------------------
; internal ram data
;--------------------------------------------------------
	.area DSEG    (DATA)
_cnt::
	.ds 1
_ksr::
	.ds 1
_previousksr::
	.ds 1
_zero_duration::
	.ds 1
_random_num::
	.ds 4
_gx_data::
	.ds 5
_tx_data::
	.ds 5
_rx_data::
	.ds 5
_pos::
	.ds 2
_idx::
	.ds 2
_seg::
	.ds 4
_AA::
	.ds 1
_BB::
	.ds 1
_seven_segment:
	.ds 17
_Digits::
	.ds 8
_arr::
	.ds 4
_uart_isr_i_50000_78:
	.ds 2
;--------------------------------------------------------
; overlayable items in internal ram
;--------------------------------------------------------
	.area	OSEG    (OVR,DATA)
_displayDigit_PARM_2:
	.ds 1
	.area	OSEG    (OVR,DATA)
	.area	OSEG    (OVR,DATA)
	.area	OSEG    (OVR,DATA)
_KeyScan_tmp_10000_45:
	.ds 1
	.area	OSEG    (OVR,DATA)
_updateDigits_PARM_2:
	.ds 3
_updateDigits_PARM_3:
	.ds 3
_updateDigits_ksr_10000_54:
	.ds 1
;--------------------------------------------------------
; Stack segment in internal ram
;--------------------------------------------------------
	.area SSEG
__start__stack:
	.ds	1

;--------------------------------------------------------
; indirectly addressable internal ram data
;--------------------------------------------------------
	.area ISEG    (DATA)
;--------------------------------------------------------
; absolute internal ram data
;--------------------------------------------------------
	.area IABS    (ABS,DATA)
	.area IABS    (ABS,DATA)
;--------------------------------------------------------
; bit data
;--------------------------------------------------------
	.area BSEG    (BIT)
;--------------------------------------------------------
; paged external ram data
;--------------------------------------------------------
	.area PSEG    (PAG,XDATA)
;--------------------------------------------------------
; uninitialized external ram data
;--------------------------------------------------------
	.area XSEG    (XDATA)
;--------------------------------------------------------
; absolute external ram data
;--------------------------------------------------------
	.area XABS    (ABS,XDATA)
;--------------------------------------------------------
; initialized external ram data
;--------------------------------------------------------
	.area XISEG   (XDATA)
	.area HOME    (CODE)
	.area GSINIT0 (CODE)
	.area GSINIT1 (CODE)
	.area GSINIT2 (CODE)
	.area GSINIT3 (CODE)
	.area GSINIT4 (CODE)
	.area GSINIT5 (CODE)
	.area GSINIT  (CODE)
	.area GSFINAL (CODE)
	.area CSEG    (CODE)
;--------------------------------------------------------
; interrupt vector
;--------------------------------------------------------
	.area HOME    (CODE)
__interrupt_vect:
	ljmp	__sdcc_gsinit_startup
	reti
	.ds	7
	ljmp	_Timer0_ISR
	.ds	5
	reti
	.ds	7
	reti
	.ds	7
	ljmp	_uart_isr
;--------------------------------------------------------
; global & static initialisations
;--------------------------------------------------------
	.area HOME    (CODE)
	.area GSINIT  (CODE)
	.area GSFINAL (CODE)
	.area GSINIT  (CODE)
	.globl __sdcc_gsinit_startup
	.globl __sdcc_program_startup
	.globl __start__stack
	.globl __mcs51_genXINIT
	.globl __mcs51_genXRAMCLEAR
	.globl __mcs51_genRAMCLEAR
;	uart.c:4: unsigned char cnt = 0;
	mov	_cnt,#0x00
;	uart.c:5: unsigned char ksr = 0;
	mov	_ksr,#0x00
;	uart.c:6: unsigned char previousksr = 0;
	mov	_previousksr,#0x00
;	uart.c:7: unsigned char zero_duration = 0;
	mov	_zero_duration,#0x00
;	uart.c:15: unsigned int pos = 0;                                                    // 紀錄7seg顯示位置
	clr	a
	mov	_pos,a
	mov	(_pos + 1),a
;	uart.c:16: unsigned int idx = 0;                                                    // 紀錄接收的數量
	mov	_idx,a
	mov	(_idx + 1),a
;	uart.c:17: unsigned char seg[4] = {0b11111111, 0b11111111, 0b11111111, 0b11111111}; // 紀錄keypad讀取轉7 Segment
	mov	_seg,#0xff
	mov	(_seg + 0x0001),#0xff
	mov	(_seg + 0x0002),#0xff
	mov	(_seg + 0x0003),#0xff
;	uart.c:18: unsigned char AA = 0;
	mov	_AA,a
;	uart.c:19: unsigned char BB = 0;
	mov	_BB,a
;	uart.c:27: static unsigned char seven_segment[17] = {
	mov	_seven_segment,#0x3f
	mov	(_seven_segment + 0x0001),#0x06
	mov	(_seven_segment + 0x0002),#0x5b
	mov	(_seven_segment + 0x0003),#0x4f
	mov	(_seven_segment + 0x0004),#0x66
	mov	(_seven_segment + 0x0005),#0x6d
	mov	(_seven_segment + 0x0006),#0x7d
	mov	(_seven_segment + 0x0007),#0x07
	mov	(_seven_segment + 0x0008),#0x7f
	mov	(_seven_segment + 0x0009),#0x6f
	mov	(_seven_segment + 0x000a),#0x77
	mov	(_seven_segment + 0x000b),#0x7c
	mov	(_seven_segment + 0x000c),#0x39
	mov	(_seven_segment + 0x000d),#0x5e
	mov	(_seven_segment + 0x000e),#0x79
	mov	(_seven_segment + 0x000f),#0x71
	mov	(_seven_segment + 0x0010),a
;	uart.c:34: unsigned char arr[] = {0b00001110, 0b00001101, 0b00001011, 0b00000111};
	mov	_arr,#0x0e
	mov	(_arr + 0x0001),#0x0d
	mov	(_arr + 0x0002),#0x0b
	mov	(_arr + 0x0003),#0x07
	.area GSFINAL (CODE)
	ljmp	__sdcc_program_startup
;--------------------------------------------------------
; Home
;--------------------------------------------------------
	.area HOME    (CODE)
	.area HOME    (CODE)
__sdcc_program_startup:
	ljmp	_main
;	return from main will return to caller
;--------------------------------------------------------
; code
;--------------------------------------------------------
	.area CSEG    (CODE)
;------------------------------------------------------------
;Allocation info for local variables in function 'displayDigit'
;------------------------------------------------------------
;position                  Allocated with name '_displayDigit_PARM_2'
;digit                     Allocated to registers 
;------------------------------------------------------------
;	uart.c:21: void displayDigit(unsigned char digit, unsigned char position) // display
;	-----------------------------------------
;	 function displayDigit
;	-----------------------------------------
_displayDigit:
	ar7 = 0x07
	ar6 = 0x06
	ar5 = 0x05
	ar4 = 0x04
	ar3 = 0x03
	ar2 = 0x02
	ar1 = 0x01
	ar0 = 0x00
	mov	_P2,dpl
;	uart.c:24: P1 = 7 - position;
	mov	r7,_displayDigit_PARM_2
	mov	a,#0x07
	clr	c
	subb	a,r7
	mov	_P1,a
;	uart.c:25: }
	ret
;------------------------------------------------------------
;Allocation info for local variables in function 'send'
;------------------------------------------------------------
;i                         Allocated to registers r7 
;i                         Allocated to registers r7 
;------------------------------------------------------------
;	uart.c:35: void send(void)
;	-----------------------------------------
;	 function send
;	-----------------------------------------
_send:
;	uart.c:37: for (unsigned char i = 0; i < 4; i++)
	mov	r7,#0x00
00107$:
	cjne	r7,#0x04,00152$
00152$:
	jnc	00101$
;	uart.c:39: Digits[i] = 0b00000000;
	mov	a,r7
	add	a, #_Digits
	mov	r0,a
	mov	@r0,#0x00
;	uart.c:37: for (unsigned char i = 0; i < 4; i++)
	inc	r7
	sjmp	00107$
00101$:
;	uart.c:42: for (unsigned char i = 0; i < 5; i++)
	mov	r7,#0x00
00110$:
	cjne	r7,#0x05,00154$
00154$:
	jnc	00112$
;	uart.c:44: TI = 0;
;	assignBit
	clr	_TI
;	uart.c:45: SBUF = gx_data[i];
	mov	a,r7
	add	a, #_gx_data
	mov	r1,a
	mov	_SBUF,@r1
;	uart.c:46: while (!TI)
00102$:
	jnb	_TI,00102$
;	uart.c:42: for (unsigned char i = 0; i < 5; i++)
	inc	r7
	sjmp	00110$
00112$:
;	uart.c:49: }
	ret
;------------------------------------------------------------
;Allocation info for local variables in function 'txsend'
;------------------------------------------------------------
;i                         Allocated to registers r6 r7 
;------------------------------------------------------------
;	uart.c:50: void txsend(void)
;	-----------------------------------------
;	 function txsend
;	-----------------------------------------
_txsend:
;	uart.c:52: for (int i = 0; i < 5; i++)
	mov	r6,#0x00
	mov	r7,#0x00
00106$:
	clr	c
	mov	a,r6
	subb	a,#0x05
	mov	a,r7
	xrl	a,#0x80
	subb	a,#0x80
	jnc	00108$
;	uart.c:54: TI = 0;
;	assignBit
	clr	_TI
;	uart.c:55: SBUF = tx_data[i];
	mov	a,r6
	add	a, #_tx_data
	mov	r1,a
	mov	_SBUF,@r1
;	uart.c:56: while (!TI)
00101$:
	jnb	_TI,00101$
;	uart.c:52: for (int i = 0; i < 5; i++)
	inc	r6
	cjne	r6,#0x00,00106$
	inc	r7
	sjmp	00106$
00108$:
;	uart.c:59: }
	ret
;------------------------------------------------------------
;Allocation info for local variables in function 'KeyScan'
;------------------------------------------------------------
;tmp                       Allocated with name '_KeyScan_tmp_10000_45'
;tmp2                      Allocated to registers r6 
;i                         Allocated to registers r5 
;fts                       Allocated to registers r4 
;ztt                       Allocated to registers r2 
;j                         Allocated to registers 
;------------------------------------------------------------
;	uart.c:60: unsigned char KeyScan(void) // keyscan
;	-----------------------------------------
;	 function KeyScan
;	-----------------------------------------
_KeyScan:
;	uart.c:62: unsigned char tmp = 4;
	mov	_KeyScan_tmp_10000_45,#0x04
;	uart.c:63: unsigned char tmp2 = 0;
	mov	r6,#0x00
;	uart.c:64: for (unsigned char i = 0; i < 4; i++)
	mov	r5,#0x00
00113$:
	cjne	r5,#0x04,00168$
00168$:
	jnc	00108$
;	uart.c:66: P0 = (~(1 << i)) | 0xf0;
	mov	b,r5
	inc	b
	mov	a,#0x01
	sjmp	00171$
00170$:
	add	a,acc
00171$:
	djnz	b,00170$
	cpl	a
	mov	r4,a
	mov	a,#0xf0
	orl	a,r4
	mov	_P0,a
;	uart.c:67: unsigned char fts = P0; // four to seven
	mov	r4,_P0
;	uart.c:68: unsigned char ztt = P0; // zero to three
	mov	r3,_P0
;	uart.c:69: fts = (fts >> 4);
	mov	a,r4
	swap	a
	anl	a,#0x0f
	mov	r4,a
;	uart.c:70: if ((P0 | 0x0f) != 0xff)
	mov	a,#0x0f
	orl	a,_P0
	mov	r2,a
	cjne	r2,#0xff,00172$
	sjmp	00122$
00172$:
;	uart.c:72: ztt = (ztt << 4);
	mov	ar2,r3
	mov	a,r2
	swap	a
	anl	a,#0xf0
;	uart.c:73: ztt = (ztt >> 4);
	swap	a
	anl	a,#0x0f
	mov	r3,a
;	uart.c:75: for (unsigned char j = 0; j < 4; j++)
00122$:
	mov	r2,#0x00
00110$:
	cjne	r2,#0x04,00173$
00173$:
	jnc	00114$
;	uart.c:77: if (arr[j] == ztt)
	mov	a,r2
	add	a, #_arr
	mov	r1,a
	mov	a,@r1
	cjne	a,ar3,00104$
;	uart.c:79: tmp2 = j;
	mov	ar6,r2
00104$:
;	uart.c:81: if (arr[j] == fts)
	mov	a,r2
	add	a, #_arr
	mov	r1,a
	mov	a,@r1
	cjne	a,ar4,00111$
;	uart.c:83: tmp = j;
	mov	_KeyScan_tmp_10000_45,r2
00111$:
;	uart.c:75: for (unsigned char j = 0; j < 4; j++)
	inc	r2
	sjmp	00110$
00114$:
;	uart.c:64: for (unsigned char i = 0; i < 4; i++)
	inc	r5
	sjmp	00113$
00108$:
;	uart.c:87: return seven_segment[tmp * 4 + tmp2];
	mov	a,_KeyScan_tmp_10000_45
	add	a,acc
	add	a,acc
	add	a,r6
	add	a, #_seven_segment
	mov	r1,a
	mov	dpl,@r1
;	uart.c:88: }
	ret
;------------------------------------------------------------
;Allocation info for local variables in function 'updateDigits'
;------------------------------------------------------------
;previousksr               Allocated with name '_updateDigits_PARM_2'
;zero_duration             Allocated with name '_updateDigits_PARM_3'
;ksr                       Allocated with name '_updateDigits_ksr_10000_54'
;i                         Allocated to registers r3 
;i                         Allocated to registers r7 
;k                         Allocated to registers r6 
;------------------------------------------------------------
;	uart.c:89: void updateDigits(unsigned char ksr, unsigned char *previousksr, unsigned char *zero_duration)
;	-----------------------------------------
;	 function updateDigits
;	-----------------------------------------
_updateDigits:
	mov	_updateDigits_ksr_10000_54,dpl
;	uart.c:91: if (*zero_duration == 0 && ksr != 0b00000000) // debounce
	mov	r4,_updateDigits_PARM_3
	mov	r5,(_updateDigits_PARM_3 + 1)
	mov	r6,(_updateDigits_PARM_3 + 2)
	mov	dpl,r4
	mov	dph,r5
	mov	b,r6
	lcall	__gptrget
	jnz	00103$
	mov	a,_updateDigits_ksr_10000_54
	jz	00103$
;	uart.c:93: for (unsigned char i = 3; i > 0; i--)
	mov	r3,#0x03
00115$:
	mov	a,r3
	jz	00101$
;	uart.c:95: Digits[i] = Digits[i - 1];
	mov	a,r3
	add	a, #_Digits
	mov	r1,a
	mov	ar2,r3
	mov	a,r2
	dec	a
	add	a, #_Digits
	mov	r0,a
	mov	ar2,@r0
	mov	@r1,ar2
;	uart.c:93: for (unsigned char i = 3; i > 0; i--)
	dec	r3
	sjmp	00115$
00101$:
;	uart.c:97: Digits[0] = ksr;
	mov	_Digits,_updateDigits_ksr_10000_54
;	uart.c:98: *previousksr = ksr;
	mov	r2,_updateDigits_PARM_2
	mov	r3,(_updateDigits_PARM_2 + 1)
	mov	r7,(_updateDigits_PARM_2 + 2)
	mov	dpl,r2
	mov	dph,r3
	mov	b,r7
	mov	a,_updateDigits_ksr_10000_54
	lcall	__gptrput
00103$:
;	uart.c:100: if (ksr == *previousksr)
	mov	r2,_updateDigits_PARM_2
	mov	r3,(_updateDigits_PARM_2 + 1)
	mov	r7,(_updateDigits_PARM_2 + 2)
	mov	dpl,r2
	mov	dph,r3
	mov	b,r7
	lcall	__gptrget
	cjne	a,_updateDigits_ksr_10000_54,00106$
;	uart.c:102: (*zero_duration)++;
	mov	dpl,r4
	mov	dph,r5
	mov	b,r6
	lcall	__gptrget
	mov	r7,a
	inc	r7
	mov	dpl,r4
	mov	dph,r5
	mov	b,r6
	mov	a,r7
	lcall	__gptrput
	sjmp	00107$
00106$:
;	uart.c:106: *zero_duration = 0;
	mov	dpl,r4
	mov	dph,r5
	mov	b,r6
	clr	a
	lcall	__gptrput
00107$:
;	uart.c:108: if (*zero_duration > 100)
	mov	dpl,r4
	mov	dph,r5
	mov	b,r6
	lcall	__gptrget
	add	a,#0xff - 0x64
	jnc	00109$
;	uart.c:110: *zero_duration = 1;
	mov	dpl,r4
	mov	dph,r5
	mov	b,r6
	mov	a,#0x01
	lcall	__gptrput
00109$:
;	uart.c:112: gx_data[0] = 'G';
	mov	_gx_data,#0x47
;	uart.c:113: for (unsigned char i = 0; i < 10; i++)
	mov	r7,#0x00
00121$:
	cjne	r7,#0x0a,00202$
00202$:
	jnc	00123$
;	uart.c:115: for (unsigned char k = 0; k < 4; k++)
	mov	a,r7
	add	a, #_seven_segment
	mov	r1,a
	mov	r6,#0x00
00118$:
	cjne	r6,#0x04,00204$
00204$:
	jnc	00122$
;	uart.c:117: if (Digits[k] == seven_segment[i])
	mov	a,r6
	add	a, #_Digits
	mov	r0,a
	mov	ar5,@r0
	mov	ar4,@r1
	mov	a,r5
	cjne	a,ar4,00119$
;	uart.c:119: gx_data[4 - k] = i + 0x30;
	mov	ar5,r6
	mov	a,#0x04
	clr	c
	subb	a,r5
	add	a, #_gx_data
	mov	r0,a
	mov	ar5,r7
	mov	a,#0x30
	add	a, r5
	mov	@r0,a
00119$:
;	uart.c:115: for (unsigned char k = 0; k < 4; k++)
	inc	r6
	sjmp	00118$
00122$:
;	uart.c:113: for (unsigned char i = 0; i < 10; i++)
	inc	r7
	sjmp	00121$
00123$:
;	uart.c:123: }
	ret
;------------------------------------------------------------
;Allocation info for local variables in function 'Timer0_ISR'
;------------------------------------------------------------
;	uart.c:125: void Timer0_ISR(void) __interrupt(1) __using(1)
;	-----------------------------------------
;	 function Timer0_ISR
;	-----------------------------------------
_Timer0_ISR:
	ar7 = 0x0f
	ar6 = 0x0e
	ar5 = 0x0d
	ar4 = 0x0c
	ar3 = 0x0b
	ar2 = 0x0a
	ar1 = 0x09
	ar0 = 0x08
	push	bits
	push	acc
	push	b
	push	dpl
	push	dph
	push	(0+7)
	push	(0+6)
	push	(0+5)
	push	(0+4)
	push	(0+3)
	push	(0+2)
	push	(0+1)
	push	(0+0)
	push	psw
	mov	psw,#0x08
;	uart.c:127: TH0 = (65536 - 6250) / 256;
	mov	_TH0,#0xe7
;	uart.c:128: TL0 = (65536 - 6250) % 256;
	mov	_TL0,#0x96
;	uart.c:129: displayDigit(Digits[cnt], cnt);
	mov	a,_cnt
	add	a, #_Digits
	mov	r1,a
	mov	dpl,@r1
	mov	_displayDigit_PARM_2,_cnt
	mov	psw,#0x00
	lcall	_displayDigit
	mov	psw,#0x08
;	uart.c:130: cnt++; // interrupt counter + 1
	inc	_cnt
;	uart.c:131: }
	pop	psw
	pop	(0+0)
	pop	(0+1)
	pop	(0+2)
	pop	(0+3)
	pop	(0+4)
	pop	(0+5)
	pop	(0+6)
	pop	(0+7)
	pop	dph
	pop	dpl
	pop	b
	pop	acc
	pop	bits
	reti
;------------------------------------------------------------
;Allocation info for local variables in function 'UART_init'
;------------------------------------------------------------
;	uart.c:132: void UART_init(void)
;	-----------------------------------------
;	 function UART_init
;	-----------------------------------------
_UART_init:
	ar7 = 0x07
	ar6 = 0x06
	ar5 = 0x05
	ar4 = 0x04
	ar3 = 0x03
	ar2 = 0x02
	ar1 = 0x01
	ar0 = 0x00
;	uart.c:134: TMOD = 0x21; // Timer_1 Mode 2, Timer_0 Mode 1
	mov	_TMOD,#0x21
;	uart.c:135: T2CON = 0x34;
	mov	_T2CON,#0x34
;	uart.c:137: TH0 = (65536 - 6250) / 256; // 表示計數 6250 步後觸發中斷
	mov	_TH0,#0xe7
;	uart.c:138: TL0 = (65536 - 6250) % 256;
	mov	_TL0,#0x96
;	uart.c:139: ET0 = 1; // 啟動 Timer 0 中斷
;	assignBit
	setb	_ET0
;	uart.c:140: TR0 = 1; // 啟動 Timer_0
;	assignBit
	setb	_TR0
;	uart.c:143: RCAP2H = 0xFF;
	mov	_RCAP2H,#0xff
;	uart.c:144: RCAP2L = 0xD9;
	mov	_RCAP2L,#0xd9
;	uart.c:145: TH2 = RCAP2H;
	mov	_TH2,_RCAP2H
;	uart.c:146: TL2 = RCAP2L;
	mov	_TL2,_RCAP2L
;	uart.c:147: TR2 = 1; // 啟動 Timer_1
;	assignBit
	setb	_TR2
;	uart.c:149: SCON = 0x50; // SM0=0,SM1=1 Mode 1 , 10 bit. REN=1 Enable receive data
	mov	_SCON,#0x50
;	uart.c:150: ES = 1;      // 致能串列埠中斷
;	assignBit
	setb	_ES
;	uart.c:151: EA = 1;      // 啟動中斷
;	assignBit
	setb	_EA
;	uart.c:152: }
	ret
;------------------------------------------------------------
;Allocation info for local variables in function 'reset'
;------------------------------------------------------------
;	uart.c:154: void reset(void)
;	-----------------------------------------
;	 function reset
;	-----------------------------------------
_reset:
;	uart.c:156: cnt = 0;
;	uart.c:157: idx = 0;
	clr	a
	mov	_cnt,a
	mov	_idx,a
	mov	(_idx + 1),a
;	uart.c:158: pos = 0;
	mov	_pos,a
	mov	(_pos + 1),a
;	uart.c:176: random_num[0] = 1;
	mov	_random_num,#0x01
;	uart.c:177: random_num[1] = 2;
	mov	(_random_num + 0x0001),#0x02
;	uart.c:178: random_num[2] = 3;
	mov	(_random_num + 0x0002),#0x03
;	uart.c:179: random_num[3] = 4;
	mov	(_random_num + 0x0003),#0x04
;	uart.c:180: }
	ret
;------------------------------------------------------------
;Allocation info for local variables in function 'uart_isr'
;------------------------------------------------------------
;i                         Allocated with name '_uart_isr_i_50000_78'
;j                         Allocated to registers r4 r5 
;------------------------------------------------------------
;	uart.c:182: void uart_isr(void) __interrupt(4) __using(3)
;	-----------------------------------------
;	 function uart_isr
;	-----------------------------------------
_uart_isr:
	ar7 = 0x1f
	ar6 = 0x1e
	ar5 = 0x1d
	ar4 = 0x1c
	ar3 = 0x1b
	ar2 = 0x1a
	ar1 = 0x19
	ar0 = 0x18
	push	bits
	push	acc
	push	b
	push	dpl
	push	dph
	push	(0+7)
	push	(0+6)
	push	(0+5)
	push	(0+4)
	push	(0+3)
	push	(0+2)
	push	(0+1)
	push	(0+0)
	push	psw
	mov	psw,#0x18
;	uart.c:185: if (RI)
;	uart.c:187: RI = 0;
;	assignBit
	jbc	_RI,00208$
	ljmp	00126$
00208$:
;	uart.c:189: rx_data[idx] = SBUF;
	mov	a,_idx
	add	a, #_rx_data
	mov	r0,a
	mov	@r0,_SBUF
;	uart.c:190: idx++;
	inc	_idx
	clr	a
	cjne	a,_idx,00209$
	inc	(_idx + 1)
00209$:
;	uart.c:191: if (idx == 5)
	mov	a,#0x05
	cjne	a,_idx,00210$
	clr	a
	cjne	a,(_idx + 1),00210$
	sjmp	00211$
00210$:
	ljmp	00126$
00211$:
;	uart.c:195: switch (rx_data[0])
	mov	r7,_rx_data
	cjne	r7,#0x41,00212$
	ljmp	00112$
00212$:
	cjne	r7,#0x47,00213$
	sjmp	00101$
00213$:
	cjne	r7,#0x52,00214$
	ljmp	00111$
00214$:
	cjne	r7,#0x5a,00215$
	ljmp	00113$
00215$:
	ljmp	00115$
;	uart.c:197: case 'G':
00101$:
;	uart.c:200: tx_data[0] = 'R';
	mov	_tx_data,#0x52
;	uart.c:201: tx_data[1] = '0';
	mov	(_tx_data + 0x0001),#0x30
;	uart.c:202: tx_data[2] = 'A';
	mov	(_tx_data + 0x0002),#0x41
;	uart.c:203: tx_data[3] = '0';
	mov	(_tx_data + 0x0003),#0x30
;	uart.c:204: tx_data[4] = 'B';
	mov	(_tx_data + 0x0004),#0x42
;	uart.c:205: for (int i = 0; i < 4; i++)
	clr	a
	mov	_uart_isr_i_50000_78,a
	mov	(_uart_isr_i_50000_78 + 1),a
00124$:
	clr	c
	mov	a,_uart_isr_i_50000_78
	subb	a,#0x04
	mov	a,(_uart_isr_i_50000_78 + 1)
	xrl	a,#0x80
	subb	a,#0x80
	jnc	00108$
;	uart.c:207: for (int j = 1; j < 5; j++)
	mov	a,_uart_isr_i_50000_78
	add	a, #_random_num
	mov	r1,a
	mov	r4,#0x01
	mov	r5,#0x00
00121$:
	clr	c
	mov	a,r4
	subb	a,#0x05
	mov	a,r5
	xrl	a,#0x80
	subb	a,#0x80
	jnc	00125$
;	uart.c:209: if (random_num[i] == rx_data[j] - '0')
	mov	ar3,@r1
	mov	a,r4
	add	a, #_rx_data
	mov	r0,a
	mov	ar2,@r0
	mov	r7,#0x00
	mov	a,r2
	add	a,#0xd0
	mov	r2,a
	mov	a,r7
	addc	a,#0xff
	mov	r7,a
	mov	r6,#0x00
	mov	a,r3
	cjne	a,ar2,00122$
	mov	a,r6
	cjne	a,ar7,00122$
;	uart.c:211: if (i == j - 1)
	mov	a,r4
	add	a,#0xff
	mov	r6,a
	mov	a,r5
	addc	a,#0xff
	mov	r7,a
	mov	a,r6
	cjne	a,_uart_isr_i_50000_78,00103$
	mov	a,r7
	cjne	a,(_uart_isr_i_50000_78 + 1),00103$
;	uart.c:213: tx_data[1]+=1;
	mov	a,(_tx_data + 0x0001)
	inc	a
	mov	(_tx_data + 0x0001),a
	sjmp	00122$
00103$:
;	uart.c:217: tx_data[3]+=1;
	mov	a,(_tx_data + 0x0003)
	inc	a
	mov	(_tx_data + 0x0003),a
00122$:
;	uart.c:207: for (int j = 1; j < 5; j++)
	inc	r4
	cjne	r4,#0x00,00121$
	inc	r5
	sjmp	00121$
00125$:
;	uart.c:205: for (int i = 0; i < 4; i++)
	inc	_uart_isr_i_50000_78
	clr	a
	cjne	a,_uart_isr_i_50000_78,00124$
	inc	(_uart_isr_i_50000_78 + 1)
	sjmp	00124$
00108$:
;	uart.c:225: txsend(); // tx_data = Rxxxx
	mov	psw,#0x00
	lcall	_txsend
	mov	psw,#0x18
;	uart.c:227: if (tx_data[1] == 4)
	mov	a,#0x04
	cjne	a,(_tx_data + 0x0001),00115$
;	uart.c:229: reset();
	mov	psw,#0x00
	lcall	_reset
	mov	psw,#0x18
;	uart.c:231: break;
;	uart.c:233: case 'R':
	sjmp	00115$
00111$:
;	uart.c:235: Digits[4] = seven_segment[rx_data[1] - '0'];
	mov	a,(_rx_data + 0x0001)
	add	a,#0xd0
	add	a, #_seven_segment
	mov	r1,a
	mov	ar7,@r1
	mov	(_Digits + 0x0004),r7
;	uart.c:236: Digits[5] = seven_segment[10];
	mov	(_Digits + 0x0005),(_seven_segment + 0x000a)
;	uart.c:237: Digits[6] = seven_segment[rx_data[3] - '0'];
	mov	a,(_rx_data + 0x0003)
	add	a,#0xd0
	add	a, #_seven_segment
	mov	r1,a
	mov	ar7,@r1
	mov	(_Digits + 0x0006),r7
;	uart.c:238: Digits[7] = seven_segment[11];
	mov	(_Digits + 0x0007),(_seven_segment + 0x000b)
;	uart.c:239: tx_data[0] = 'A';
	mov	_tx_data,#0x41
;	uart.c:240: txsend(); // 得到回覆後換對方猜
	mov	psw,#0x00
	lcall	_txsend
	mov	psw,#0x18
;	uart.c:242: case 'A':
00112$:
;	uart.c:244: TI = 0;
;	assignBit
	clr	_TI
;	uart.c:245: break;
;	uart.c:247: case 'Z':
	sjmp	00115$
00113$:
;	uart.c:250: reset();
	mov	psw,#0x00
	lcall	_reset
	mov	psw,#0x18
;	uart.c:256: }
00115$:
;	uart.c:258: idx = 0;
	clr	a
	mov	_idx,a
	mov	(_idx + 1),a
00126$:
;	uart.c:261: }
	pop	psw
	pop	(0+0)
	pop	(0+1)
	pop	(0+2)
	pop	(0+3)
	pop	(0+4)
	pop	(0+5)
	pop	(0+6)
	pop	(0+7)
	pop	dph
	pop	dpl
	pop	b
	pop	acc
	pop	bits
	reti
;------------------------------------------------------------
;Allocation info for local variables in function 'main'
;------------------------------------------------------------
;i                         Allocated to registers r7 
;------------------------------------------------------------
;	uart.c:263: void main(void)
;	-----------------------------------------
;	 function main
;	-----------------------------------------
_main:
	ar7 = 0x07
	ar6 = 0x06
	ar5 = 0x05
	ar4 = 0x04
	ar3 = 0x03
	ar2 = 0x02
	ar1 = 0x01
	ar0 = 0x00
;	uart.c:265: UART_init();
	lcall	_UART_init
;	uart.c:266: reset();
	lcall	_reset
;	uart.c:267: while (1)
00109$:
;	uart.c:269: if (cnt >= 8) // 6250*8*1us = 0.05 second
	mov	a,#0x100 - 0x08
	add	a,_cnt
	jnc	00109$
;	uart.c:271: cnt = 0;
	mov	_cnt,#0x00
;	uart.c:272: ksr = KeyScan();
	lcall	_KeyScan
	mov	_ksr,dpl
;	uart.c:273: if (ksr == 0b01110111)
	mov	a,#0x77
	cjne	a,_ksr,00121$
;	uart.c:275: send();
	lcall	_send
;	uart.c:279: for (unsigned char i = 0; i < 10; i++)
00121$:
	mov	r7,#0x00
00112$:
	cjne	r7,#0x0a,00155$
00155$:
	jnc	00109$
;	uart.c:281: if (ksr == seven_segment[i])
	mov	a,r7
	add	a, #_seven_segment
	mov	r1,a
	mov	a,@r1
	cjne	a,_ksr,00113$
;	uart.c:283: updateDigits(ksr, &previousksr, &zero_duration);
	mov	_updateDigits_PARM_2,#_previousksr
	mov	(_updateDigits_PARM_2 + 1),#0x00
	mov	(_updateDigits_PARM_2 + 2),#0x40
	mov	_updateDigits_PARM_3,#_zero_duration
	mov	(_updateDigits_PARM_3 + 1),#0x00
	mov	(_updateDigits_PARM_3 + 2),#0x40
	mov	dpl, _ksr
	push	ar7
	lcall	_updateDigits
	pop	ar7
00113$:
;	uart.c:279: for (unsigned char i = 0; i < 10; i++)
	inc	r7
;	uart.c:288: }
	sjmp	00112$
	.area CSEG    (CODE)
	.area CONST   (CODE)
	.area XINIT   (CODE)
	.area CABS    (ABS,CODE)
