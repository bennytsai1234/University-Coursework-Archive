# 定義變量
TARGET = main
SOURCE = $(TARGET).c
OBJECT = $(TARGET).ihx
HEXFILE = $(TARGET).hex

# 默認目標
all: $(HEXFILE)

# 規則
$(HEXFILE): $(OBJECT)
	packihx $(OBJECT) > $(HEXFILE)
$(OBJECT):asmfunc.rel
	sdcc main.c asmfunc.rel
asmfunc.rel:asmfunc.asm
	sdas8051 -losg asmfunc.asm
# 清理規則
clean: 
	rm -f *.o
	rm -f *.ihx
	rm -f *.lib
	rm -f *.hex
	rm -f *.lst
	rm -f *.sym
	rm -f *.rel
	rm -f *.rst
	rm -f *.mem
	rm -f *.map
	rm -f *.lst
	rm -f *.lk



