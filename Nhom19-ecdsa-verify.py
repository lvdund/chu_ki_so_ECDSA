# Nhom 19 - Demo ECDSA - verify signature

from pycoin.ecdsa import generator_secp256k1, verify
import hashlib
import json
import pkg_resources
pkg_resources.require("pycoin==0.80")


def sha3_256Hash(msg):
    hashBytes = hashlib.sha3_256(msg.encode("utf8")).digest()
    return int.from_bytes(hashBytes, byteorder="big")


def verifyECDSAsecp256k1(msg, signature, pubKey):
    msgHash = sha3_256Hash(msg)
    valid = verify(generator_secp256k1, pubKey, msgHash, signature)
    return valid


def main():
    # read data from JSON file
    with open("ecdsa.json", "r") as json_file:
        data = json.load(json_file)
    msg = data["msg"]
    print("Received message:", msg)
    pubKey = data["pubKey"]
    print(f"Received pubkey: ({hex(pubKey[0])}, {hex(pubKey[1])})")
    signature = data["signature"]
    print("Received signature: r=" +
          hex(signature[0]) + ", s=" + hex(signature[1]))

    # verify signature
    valid = verifyECDSAsecp256k1(msg, signature, pubKey)
    print("Signature valid?", valid)
    input()


if __name__ == "__main__":
    main()
