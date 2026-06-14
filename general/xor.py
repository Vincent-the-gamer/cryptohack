# https://cryptohack.org/challenges/general/

from pwn import xor

str = "label"

converted = "".join([xor(ord(c), 13).decode() for c in str])

print(f"crypto{{{converted}}}")
