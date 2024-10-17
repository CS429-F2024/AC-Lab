# GCC=aarch64-linux-gnu-gcc
# AR=aarch64-linux-gnu-ar
GCC=gcc
AR=ar
AC_GCC_ARGS=-O3 -static

.PHONY: ac

ac: testbench.a
	$(GCC) testbench.a functions.s -ggdb -o ac

.PHONY: verify

verify:
	python3 verify.py functions.s
	@lines=$$(python3 verify.py functions.s | wc -l); \
	half=$$((lines / 2)); \
	echo "Total number of errors: $$half"

clean: 
	rm -f *.o ac

