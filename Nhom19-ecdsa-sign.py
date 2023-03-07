# Nhom 19 - Demo ECDSA - sign message

from pycoin.ecdsa import generator_secp256k1, sign
import hashlib
import secrets
import json
import pkg_resources
pkg_resources.require("pycoin==0.80")


def sha3_256Hash(msg):
    hashBytes = hashlib.sha3_256(msg.encode("utf8")).digest()
    return int.from_bytes(hashBytes, byteorder="big")


def signECDSAsecp256k1(msg, privKey):
    msgHash = sha3_256Hash(msg)
    signature = sign(generator_secp256k1, privKey, msgHash)
    return signature


def main():
    msg = input("Message for ECDSA signing: ")
    privKey = secrets.randbelow(generator_secp256k1.order())
    pubKey = (generator_secp256k1 * privKey).pair()
    print("Private key:", hex(privKey))
    print("Public key: (" + hex(pubKey[0]) + ", " + hex(pubKey[1]) + ")")

    # sign message
    signature = signECDSAsecp256k1(msg, privKey)
    print("Signature: r=" + hex(signature[0]) + ", s=" + hex(signature[1]))

    # save data to JSON file
    data = {
        "msg": msg,
        "pubKey": pubKey,
        "signature": signature
    }
    json_object = json.dumps(data, indent=4)

    with open("ecdsa.json", "w") as outfile:
        outfile.write(json_object)
    print("Data saved to ecdsa.json")


if __name__ == "__main__":
    main()
