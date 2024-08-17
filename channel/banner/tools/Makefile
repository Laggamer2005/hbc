# Specify the prefix for the compiler and strip commands
PREFIX ?= /

# Set the compiler flags for optimization, warnings, and include/library paths
CFLAGS = -O3 -Wall -I/usr/local/include -L/usr/local/lib

# Set the compiler and strip commands
CC = $(PREFIX)gcc
STRIP = $(PREFIX)strip

# Define the executable extension (e.g., .exe on Windows, empty on Unix-like systems)
EXE ?=

# The main target: build all executables
all: mkbns$(EXE) png2tpl$(EXE) lz77$(EXE)

# Build mkbns executable
mkbns$(EXE): mkbns.c
    $(CC) $(CFLAGS) -o $@ $< -lm

# Build png2tpl executable
png2tpl$(EXE): png2tpl.c
    $(CC) $(CFLAGS) -o $@ $< -lpng

# Build lz77 executable
lz77$(EXE): lz77.c
    $(CC) $(CFLAGS) -o $@ $<

# Clean up object files and executables
clean:
    rm -f mkbns$(EXE) png2tpl$(EXE) lz77$(EXE)

# Remove object files (not generated in this case, but good practice)
    rm -f *.o
