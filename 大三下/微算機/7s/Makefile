# 定義變量
TARGET = 7s
SOURCE = $(TARGET).c
OBJECT = $(TARGET).ihx
HEXFILE = $(TARGET).hex

# 默認目標
all: $(HEXFILE)

# 規則
$(HEXFILE): $(OBJECT)
	packihx $(OBJECT) > $(HEXFILE)

$(OBJECT): $(SOURCE)
	sdcc $(SOURCE)

# 清理規則
clean:
    # 清理中間文件和生成的 HEX 文件
	rm -f $(OBJECT) $(HEXFILE) $(TARGET).lst $(TARGET).map $(TARGET).mem $(TARGET).asm $(TARGET).lk $(TARGET).rel $(TARGET).rst $(TARGET).sym