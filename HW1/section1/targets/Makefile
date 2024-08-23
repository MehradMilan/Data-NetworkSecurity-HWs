# tools
CC := gcc
RM := rm -f
EXECSTACK := execstack

# flags
CFLAGS := -ggdb -m32 -g -std=c99 -D_GNU_SOURCE -fno-stack-protector -mpreferred-stack-boundary=2 -Wno-format-security
LDFLAGS := -m32
LDLIBS :=

# sources
sources := target1.c target2.c tmalloc.c
targets := target1 target2

# gmake magic
.PHONY: default all clean

#targets
default: all
all: mkexecstack

mkexecstack: $(targets)
	$(EXECSTACK) -s $(targets)

install: mkexecstack
	install -o root -t /tmp $(targets)
	chmod 4755 /tmp/target*

%.bin: %.o
	objcopy -S -O binary -j .text $< $@

%.o: %.c
	$(CC) $< -c -o $@ $(CFLAGS)

%.o: %.S
	$(CC) $< -c -o $@ $(CFLAGS)

clean:
	$(RM) $(targets) $(sources:.c=.o)
