;--------------------------------------------------------
; File Created by SDCC : free open source ISO C Compiler 
; Version 4.4.0 #14620 (MINGW64)
;--------------------------------------------------------
	.module thermo
	.optsdcc -mmcs51 --model-small
	
;--------------------------------------------------------
; Public variables in this module
;--------------------------------------------------------
	.globl _displayDigit_PARM_2
	.globl _main
	.globl _read_sensor
	.globl _writeByte_1W
	.globl _readByte_1W
	.globl _init_1W
	.globl _delay
	.globl _External_ISR
	.globl _Timer0_ISR
	.globl _t0_init
	.globl _KeyScan
	.globl _displayDigit
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
	.globl _sensorBuffer
	.globl _resolution
	.globl _arr
	.globl _Digits
	.globl _ksr
	.globl _cnt
	.globl _setResolution
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
;--------------------------------------------------------
; overlayable register banks
;--------------------------------------------------------
	.area REG_BANK_0	(REL,OVR,DATA)
	.ds 8
	.area REG_BANK_1	(REL,OVR,DATA)
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
_Digits::
	.ds 8
_seven_segment:
	.ds 18
_arr::
	.ds 4
_resolution::
	.ds 4
_sensorBuffer::
	.ds 2
;--------------------------------------------------------
; overlayable items in internal ram
;--------------------------------------------------------
	.area	OSEG    (OVR,DATA)
_displayDigit_PARM_2:
	.ds 1
	.area	OSEG    (OVR,DATA)
	.area	OSEG    (OVR,DATA)
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
	ljmp	_External_ISR
	.ds	5
	ljmp	_Timer0_ISR
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
;	thermo.c:3: unsigned char cnt = 0;
	mov	_cnt,#0x00
;	thermo.c:4: char ksr = 0;
	mov	_ksr,#0x00
;	thermo.c:7: static unsigned char seven_segment[18] = {
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
	mov	(_seven_segment + 0x0010),#0x00
	mov	(_seven_segment + 0x0011),#0x80
;	thermo.c:14: unsigned char arr[] = {0b00001110, 0b00001101, 0b00001011, 0b00000111};
	mov	_arr,#0x0e
	mov	(_arr + 0x0001),#0x0d
	mov	(_arr + 0x0002),#0x0b
	mov	(_arr + 0x0003),#0x07
;	thermo.c:82: unsigned char resolution[4] = {0, 1, 2, 3};
	mov	_resolution,#0x00
	mov	(_resolution + 0x0001),#0x01
	mov	(_resolution + 0x0002),#0x02
	mov	(_resolution + 0x0003),#0x03
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
;	thermo.c:18: void displayDigit(unsigned char digit, unsigned char position)
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
;	thermo.c:21: P1 = 7 - position;
	mov	r7,_displayDigit_PARM_2
	mov	a,#0x07
	clr	c
	subb	a,r7
	mov	_P1,a
;	thermo.c:22: }
	ret
;------------------------------------------------------------
;Allocation info for local variables in function 'KeyScan'
;------------------------------------------------------------
;tmp                       Allocated to registers r7 
;tmp2                      Allocated to registers 
;i                         Allocated to registers r6 
;fts                       Allocated to registers r5 
;ztt                       Allocated to registers 
;j                         Allocated to registers 
;------------------------------------------------------------
;	thermo.c:24: void KeyScan(void)
;	-----------------------------------------
;	 function KeyScan
;	-----------------------------------------
_KeyScan:
;	thermo.c:26: char tmp = 0b10000000;
	mov	r7,#0x80
;	thermo.c:28: for (unsigned char i = 0; i < 4; i++)
	mov	r6,#0x00
00113$:
	cjne	r6,#0x04,00162$
00162$:
	jnc	00106$
;	thermo.c:30: P0 = (~(1 << i)) | 0xf0;
	mov	b,r6
	inc	b
	mov	a,#0x01
	sjmp	00165$
00164$:
	add	a,acc
00165$:
	djnz	b,00164$
	cpl	a
	mov	r5,a
	mov	a,#0xf0
	orl	a,r5
	mov	_P0,a
;	thermo.c:31: unsigned char fts = P0; // Four to Seven bits
	mov	r5,_P0
;	thermo.c:32: unsigned char ztt = P0; // Zero to Three bits
	mov	a,_P0
;	thermo.c:33: fts = (fts >> 4) & 0x0F;
	mov	a,r5
	swap	a
	anl	a,#0x0f
	mov	r5,a
	anl	ar5,#0x0f
;	thermo.c:34: ztt = (~P0) & 0x0F;
	mov	a,_P0
;	thermo.c:36: for (unsigned char j = 0; j < 4; j++)
	mov	r4,#0x00
00110$:
	cjne	r4,#0x04,00166$
00166$:
	jnc	00114$
;	thermo.c:38: if (arr[j] == ztt)
	mov	a,r4
	add	a, #_arr
	mov	r1,a
;	thermo.c:42: if (arr[j] == fts)
	mov	a,@r1
	cjne	a,ar5,00111$
;	thermo.c:44: tmp = j;
	mov	ar7,r4
00111$:
;	thermo.c:36: for (unsigned char j = 0; j < 4; j++)
	inc	r4
	sjmp	00110$
00114$:
;	thermo.c:28: for (unsigned char i = 0; i < 4; i++)
	inc	r6
	sjmp	00113$
00106$:
;	thermo.c:48: P0 = 0xf0;
	mov	_P0,#0xf0
;	thermo.c:49: if (tmp != 0b10000000)
	cjne	r7,#0x80,00170$
	ret
00170$:
;	thermo.c:51: ksr = tmp;
	mov	_ksr,r7
;	thermo.c:53: }
	ret
;------------------------------------------------------------
;Allocation info for local variables in function 't0_init'
;------------------------------------------------------------
;	thermo.c:55: void t0_init(void)
;	-----------------------------------------
;	 function t0_init
;	-----------------------------------------
_t0_init:
;	thermo.c:57: TH0 = (65536 - 5000) / 256;
	mov	_TH0,#0xec
;	thermo.c:58: TL0 = (65536 - 5000) % 256;
	mov	_TL0,#0x78
;	thermo.c:59: TMOD = (TMOD & 0xF0) | 0x01;
	mov	a,_TMOD
	anl	a,#0xf0
	orl	a,#0x01
	mov	_TMOD,a
;	thermo.c:60: ET0 = 1;
;	assignBit
	setb	_ET0
;	thermo.c:61: TR0 = 1;
;	assignBit
	setb	_TR0
;	thermo.c:62: EA = 1;
;	assignBit
	setb	_EA
;	thermo.c:63: EX0 = 1;
;	assignBit
	setb	_EX0
;	thermo.c:64: IT0 = 1;
;	assignBit
	setb	_IT0
;	thermo.c:65: P0 = 0xf0;
	mov	_P0,#0xf0
;	thermo.c:66: }
	ret
;------------------------------------------------------------
;Allocation info for local variables in function 'Timer0_ISR'
;------------------------------------------------------------
;	thermo.c:68: void Timer0_ISR(void) __interrupt(1) __using(1)
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
;	thermo.c:70: TH0 = (65536 - 5000) / 256;
	mov	_TH0,#0xec
;	thermo.c:71: TL0 = (65536 - 5000) % 256;
	mov	_TL0,#0x78
;	thermo.c:72: IT0 = 1;
;	assignBit
	setb	_IT0
;	thermo.c:73: if (cnt >= 4)
	mov	a,#0x100 - 0x04
	add	a,_cnt
	jnc	00102$
;	thermo.c:75: cnt = 0;
	mov	_cnt,#0x00
00102$:
;	thermo.c:77: displayDigit(Digits[cnt], cnt);
	mov	a,_cnt
	add	a, #_Digits
	mov	r1,a
	mov	dpl,@r1
	mov	_displayDigit_PARM_2,_cnt
	mov	psw,#0x00
	lcall	_displayDigit
	mov	psw,#0x08
;	thermo.c:78: cnt++;
	inc	_cnt
;	thermo.c:79: EX0 = 1;
;	assignBit
	setb	_EX0
;	thermo.c:80: }
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
;Allocation info for local variables in function 'External_ISR'
;------------------------------------------------------------
;	thermo.c:84: void External_ISR(void) __interrupt(0) __using(1)
;	-----------------------------------------
;	 function External_ISR
;	-----------------------------------------
_External_ISR:
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
;	thermo.c:86: KeyScan();
	mov	psw,#0x00
	lcall	_KeyScan
	mov	psw,#0x08
;	thermo.c:87: setResolution(resolution[ksr]);
	mov	a,_ksr
	add	a, #_resolution
	mov	r1,a
	mov	dpl,@r1
	mov	psw,#0x00
	lcall	_setResolution
	mov	psw,#0x08
;	thermo.c:88: EX0 = 0;
;	assignBit
	clr	_EX0
;	thermo.c:89: }
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
;Allocation info for local variables in function 'delay'
;------------------------------------------------------------
;i                         Allocated to registers 
;------------------------------------------------------------
;	thermo.c:93: void delay(unsigned int i)
;	-----------------------------------------
;	 function delay
;	-----------------------------------------
_delay:
	ar7 = 0x07
	ar6 = 0x06
	ar5 = 0x05
	ar4 = 0x04
	ar3 = 0x03
	ar2 = 0x02
	ar1 = 0x01
	ar0 = 0x00
	mov	r6, dpl
	mov	r7, dph
;	thermo.c:95: while (i--)
00101$:
	mov	ar4,r6
	mov	ar5,r7
	dec	r6
	cjne	r6,#0xff,00113$
	dec	r7
00113$:
	mov	a,r4
	orl	a,r5
	jnz	00101$
;	thermo.c:97: }
	ret
;------------------------------------------------------------
;Allocation info for local variables in function 'init_1W'
;------------------------------------------------------------
;	thermo.c:99: void init_1W(void)
;	-----------------------------------------
;	 function init_1W
;	-----------------------------------------
_init_1W:
;	thermo.c:101: P3_3 = 1;
;	assignBit
	setb	_P3_3
;	thermo.c:102: delay(8);
	mov	dptr,#0x0008
	lcall	_delay
;	thermo.c:103: P3_3 = 0;
;	assignBit
	clr	_P3_3
;	thermo.c:104: delay(80);
	mov	dptr,#0x0050
	lcall	_delay
;	thermo.c:105: P3_3 = 1;
;	assignBit
	setb	_P3_3
;	thermo.c:106: delay(14);
	mov	dptr,#0x000e
	lcall	_delay
;	thermo.c:107: delay(20);
	mov	dptr,#0x0014
;	thermo.c:108: }
	ljmp	_delay
;------------------------------------------------------------
;Allocation info for local variables in function 'readByte_1W'
;------------------------------------------------------------
;i                         Allocated to registers r6 
;dat                       Allocated to registers r7 
;------------------------------------------------------------
;	thermo.c:110: unsigned char readByte_1W(void)
;	-----------------------------------------
;	 function readByte_1W
;	-----------------------------------------
_readByte_1W:
;	thermo.c:113: unsigned char dat = 0;
	mov	r7,#0x00
;	thermo.c:114: for (i = 8; i > 0; i--)
	mov	r6,#0x08
00104$:
;	thermo.c:116: P3_3 = 0;
;	assignBit
	clr	_P3_3
;	thermo.c:117: dat >>= 1;
	mov	a,r7
	clr	c
	rrc	a
	mov	r7,a
;	thermo.c:118: P3_3 = 1;
;	assignBit
	setb	_P3_3
;	thermo.c:119: if (P3_3)
	jnb	_P3_3,00102$
;	thermo.c:120: dat |= 0x80;
	orl	ar7,#0x80
00102$:
;	thermo.c:121: delay(4);
	mov	dptr,#0x0004
	push	ar7
	push	ar6
	lcall	_delay
	pop	ar6
	pop	ar7
;	thermo.c:114: for (i = 8; i > 0; i--)
	djnz	r6,00104$
;	thermo.c:123: return dat;
	mov	dpl, r7
;	thermo.c:124: }
	ret
;------------------------------------------------------------
;Allocation info for local variables in function 'writeByte_1W'
;------------------------------------------------------------
;dat                       Allocated to registers r7 
;i                         Allocated to registers r6 
;------------------------------------------------------------
;	thermo.c:126: void writeByte_1W(unsigned char dat)
;	-----------------------------------------
;	 function writeByte_1W
;	-----------------------------------------
_writeByte_1W:
	mov	r7, dpl
;	thermo.c:129: for (i = 8; i > 0; i--)
	mov	r6,#0x08
00102$:
;	thermo.c:131: P3_3 = 0;
;	assignBit
	clr	_P3_3
;	thermo.c:132: P3_3 = dat & 0x01;
	mov	a,r7
	anl	a,#0x01
;	assignBit
	add	a,#0xff
	mov	_P3_3,c
;	thermo.c:133: delay(5);
	mov	dptr,#0x0005
	push	ar7
	push	ar6
	lcall	_delay
	pop	ar6
	pop	ar7
;	thermo.c:134: P3_3 = 1;
;	assignBit
	setb	_P3_3
;	thermo.c:135: dat >>= 1;
	mov	a,r7
	clr	c
	rrc	a
	mov	r7,a
;	thermo.c:129: for (i = 8; i > 0; i--)
	djnz	r6,00102$
;	thermo.c:137: delay(4);
	mov	dptr,#0x0004
;	thermo.c:138: }
	ljmp	_delay
;------------------------------------------------------------
;Allocation info for local variables in function 'read_sensor'
;------------------------------------------------------------
;	thermo.c:140: void read_sensor(void)
;	-----------------------------------------
;	 function read_sensor
;	-----------------------------------------
_read_sensor:
;	thermo.c:142: init_1W();
	lcall	_init_1W
;	thermo.c:143: writeByte_1W(0xCC); // Skip ROM
	mov	dpl, #0xcc
	lcall	_writeByte_1W
;	thermo.c:144: writeByte_1W(0x44); // Convert T
	mov	dpl, #0x44
	lcall	_writeByte_1W
;	thermo.c:146: init_1W();
	lcall	_init_1W
;	thermo.c:147: writeByte_1W(0xCC); // Skip ROM
	mov	dpl, #0xcc
	lcall	_writeByte_1W
;	thermo.c:148: writeByte_1W(0xBE); // Read Scratchpad
	mov	dpl, #0xbe
	lcall	_writeByte_1W
;	thermo.c:150: sensorBuffer[0] = readByte_1W();
	lcall	_readByte_1W
	mov	a, dpl
	mov	_sensorBuffer,a
;	thermo.c:151: sensorBuffer[1] = readByte_1W();
	lcall	_readByte_1W
	mov	a, dpl
	mov	(_sensorBuffer + 0x0001),a
;	thermo.c:152: }
	ret
;------------------------------------------------------------
;Allocation info for local variables in function 'setResolution'
;------------------------------------------------------------
;resolution                Allocated to registers r7 
;------------------------------------------------------------
;	thermo.c:154: void setResolution(unsigned char resolution)
;	-----------------------------------------
;	 function setResolution
;	-----------------------------------------
_setResolution:
	mov	r7, dpl
;	thermo.c:156: init_1W();
	push	ar7
	lcall	_init_1W
;	thermo.c:157: writeByte_1W(0xCC); // Skip ROM
	mov	dpl, #0xcc
	lcall	_writeByte_1W
;	thermo.c:158: writeByte_1W(0x4E); // Write Scratchpad
	mov	dpl, #0x4e
	lcall	_writeByte_1W
;	thermo.c:161: writeByte_1W(0x00);            // TH
	mov	dpl, #0x00
	lcall	_writeByte_1W
;	thermo.c:162: writeByte_1W(0x00);            // TL
	mov	dpl, #0x00
	lcall	_writeByte_1W
	pop	ar7
;	thermo.c:163: writeByte_1W(resolution << 5); // Configuration register
	mov	a,r7
	swap	a
	rl	a
	anl	a,#0xe0
	mov	dpl,a
	lcall	_writeByte_1W
;	thermo.c:165: init_1W();
	lcall	_init_1W
;	thermo.c:166: writeByte_1W(0xCC); // Skip ROM
	mov	dpl, #0xcc
	lcall	_writeByte_1W
;	thermo.c:167: writeByte_1W(0x48); // Copy Scratchpad to EEPROM
	mov	dpl, #0x48
;	thermo.c:168: }
	ljmp	_writeByte_1W
;------------------------------------------------------------
;Allocation info for local variables in function 'main'
;------------------------------------------------------------
;returntemp                Allocated to registers 
;temperature               Allocated to registers r4 r5 r6 r7 
;temp                      Allocated to registers r6 r7 
;------------------------------------------------------------
;	thermo.c:170: void main(void)
;	-----------------------------------------
;	 function main
;	-----------------------------------------
_main:
;	thermo.c:172: t0_init();
	lcall	_t0_init
;	thermo.c:175: while (1)
00102$:
;	thermo.c:177: EA = 0;
;	assignBit
	clr	_EA
;	thermo.c:178: read_sensor();
	lcall	_read_sensor
;	thermo.c:179: EA = 1;
;	assignBit
	setb	_EA
;	thermo.c:180: returntemp = sensorBuffer[0] | (sensorBuffer[1] << 8);
	mov	r7,(_sensorBuffer + 0x0001)
	mov	r6,#0x00
	mov	r4,_sensorBuffer
	mov	r5,#0x00
	mov	a,r6
	orl	a,r4
	mov	dpl,a
	mov	a,r7
	orl	a,r5
	mov	dph,a
;	thermo.c:181: float temperature = returntemp * 0.0625;
	lcall	___sint2fs
	mov	r4, dpl
	mov	r5, dph
	mov	r6, b
	mov	r7, a
	push	ar4
	push	ar5
	push	ar6
	push	ar7
;	thermo.c:182: int temp = (int)(temperature * 100);
	mov	dptr,#0x0000
	mov	b, #0x80
	mov	a, #0x3d
	lcall	___fsmul
	mov	r4, dpl
	mov	r5, dph
	mov	r6, b
	mov	r7, a
	mov	a,sp
	add	a,#0xfc
	mov	sp,a
	push	ar4
	push	ar5
	push	ar6
	push	ar7
	mov	dptr,#0x0000
	mov	b, #0xc8
	mov	a, #0x42
	lcall	___fsmul
	mov	r4, dpl
	mov	r5, dph
	mov	r6, b
	mov	r7, a
	mov	a,sp
	add	a,#0xfc
	mov	sp,a
	mov	dpl, r4
	mov	dph, r5
	mov	b, r6
	mov	a, r7
	lcall	___fs2sint
;	thermo.c:184: Digits[0] = seven_segment[temp % 10];
	mov	r6,dpl
	mov	r7,dph
	mov	__modsint_PARM_2,#0x0a
	mov	(__modsint_PARM_2 + 1),#0x00
	push	ar7
	push	ar6
	lcall	__modsint
	mov	r4, dpl
	pop	ar6
	pop	ar7
	mov	a,r4
	add	a, #_seven_segment
	mov	r1,a
	mov	ar5,@r1
	mov	_Digits,r5
;	thermo.c:185: temp /= 10;
	mov	__divsint_PARM_2,#0x0a
	mov	(__divsint_PARM_2 + 1),#0x00
;	thermo.c:186: Digits[1] = seven_segment[temp % 10];
	mov	dpl, r6
	mov	dph, r7
	lcall	__divsint
	mov	r6,dpl
	mov	r7,dph
	mov	__modsint_PARM_2,#0x0a
	mov	(__modsint_PARM_2 + 1),#0x00
	push	ar7
	push	ar6
	lcall	__modsint
	mov	r4, dpl
	pop	ar6
	pop	ar7
	mov	a,r4
	add	a, #_seven_segment
	mov	r1,a
	mov	ar5,@r1
	mov	(_Digits + 0x0001),r5
;	thermo.c:187: temp /= 10;
	mov	__divsint_PARM_2,#0x0a
	mov	(__divsint_PARM_2 + 1),#0x00
;	thermo.c:188: Digits[2] = seven_segment[temp % 10] | seven_segment[17];
	mov	dpl, r6
	mov	dph, r7
	lcall	__divsint
	mov	r6,dpl
	mov	r7,dph
	mov	__modsint_PARM_2,#0x0a
	mov	(__modsint_PARM_2 + 1),#0x00
	push	ar7
	push	ar6
	lcall	__modsint
	mov	r4, dpl
	pop	ar6
	pop	ar7
	mov	a,r4
	add	a, #_seven_segment
	mov	r1,a
	mov	ar5,@r1
	mov	a,(_seven_segment + 0x0011)
	orl	a,r5
	mov	(_Digits + 0x0002),a
;	thermo.c:189: temp /= 10;
	mov	__divsint_PARM_2,#0x0a
	mov	(__divsint_PARM_2 + 1),#0x00
;	thermo.c:190: Digits[3] = seven_segment[temp % 10];
	mov	dpl, r6
	mov	dph, r7
	lcall	__divsint
	mov	__modsint_PARM_2,#0x0a
	mov	(__modsint_PARM_2 + 1),#0x00
	lcall	__modsint
	mov	r6, dpl
	mov	a,r6
	add	a, #_seven_segment
	mov	r1,a
	mov	ar7,@r1
	mov	(_Digits + 0x0003),r7
;	thermo.c:192: }
	ljmp	00102$
	.area CSEG    (CODE)
	.area CONST   (CODE)
	.area XINIT   (CODE)
	.area CABS    (ABS,CODE)
