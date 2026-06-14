# https://cryptohack.org/challenges/general/
import base64
import codecs
import json

from Crypto.Util.number import long_to_bytes
from pwn import *

r = remote("socket.cryptohack.org", 13377, level="debug")


def json_recv():
    line = r.recvline()
    return json.loads(line.decode())


def json_send(hsh):
    request = json.dumps(hsh).encode()
    r.sendline(request)


for i in range(0, 101):
    received = json_recv()

    print("Received type: ")
    print(received["type"])

    # to_send = {"decoded": "changeme"}
    to_send = {"decoded": ""}

    if received["type"]:
        if received["type"] == "hex":
            decoded = bytes.fromhex(received["encoded"]).decode()
            to_send = {"decoded": decoded}
        elif received["type"] == "base64":
            decoded = base64.b64decode(received["encoded"]).decode()
            to_send = {"decoded": decoded}
        elif received["type"] == "rot13":
            decoded = codecs.decode(received["encoded"], "rot_13")
            to_send = {"decoded": decoded}
        elif received["type"] == "bigint":
            data = received["encoded"]
            if data.startswith("0x"):
                data = data[2:]
            decoded = long_to_bytes(int(data, 16)).decode()
            to_send = {"decoded": decoded}
        elif received["type"] == "utf-8":
            decoded = "".join([chr(i) for i in received["encoded"]])
            to_send = {"decoded": decoded}
    elif received["flag"]:
        print("Received flag:")
        print(received["flag"])
        break

    print("Received encoded value: ")
    print(received["encoded"])

    json_send(to_send)
