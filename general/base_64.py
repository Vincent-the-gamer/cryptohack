# https://cryptohack.org/challenges/general/
import base64

str = "72bca9b68fc16ac7beeb8f849dca1d8a783e8acf9679bf9269f7bf"

b_str = bytes.fromhex(str)

base64_str = base64.b64encode(b_str).decode()

print(base64_str)
