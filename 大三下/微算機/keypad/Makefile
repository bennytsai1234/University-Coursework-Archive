LIB_NAME = myIO.lib
TARGET = Lab3-main

all: $(TARGET).hex

LED_Display.o: LED_Display.c
	sdcc -c LED_Display.c -o LED_Display.o

Keypad4x4.o: Keypad4x4.c
	sdcc -c Keypad4x4.c -o Keypad4x4.o

#將目標檔打包成庫
$(LIB_NAME): LED_Display.o Keypad4x4.o
	$(AR) -rc $(LIB_NAME) LED_Display.o Keypad4x4.o
	sdranlib $(LIB_NAME)

# 編譯主程式
$(TARGET).ihx: $(TARGET).c $(LIB_NAME)
	sdcc  $(TARGET).c $(LIB_NAME) -o $(TARGET).ihx

# 產生.hex檔案
$(TARGET).hex: $(TARGET).ihx
	packihx $(TARGET).ihx > $(TARGET).hex


# 清理規則
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
