TARGET = uart

all: $(TARGET).hex

$(TARGET).hex: $(TARGET).ihx
	packihx $(TARGET).ihx > $(TARGET).hex
$(TARGET).ihx: $(TARGET).c 
	sdcc $(TARGET).c
clean: 
	rm -f *.o
	rm -f *.ihx
	rm -f *.lib
	rm -f *.hex
	rm -f *.lst
	rm -f *.sym
	rm -f *.asm
	rm -f *.rel
	rm -f *.rst
	rm -f *.mem
	rm -f *.map
	rm -f *.lst
	rm -f *.lk