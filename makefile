CC = gcc
CFLAGS = -pedantic -errors -Wall -c -std=gnu99 

all: FindLink

FindLink: FindLink.o
	 $(CC) -o FindLink FindLink.o -lm -lpthread -lrt

FindLink.o: FindLink.c
	 $(CC) $(CFLAGS) FindLink.c

clean: 
	rm *.o FindLink
