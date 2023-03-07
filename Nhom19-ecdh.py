# Nhom 19 - Demo ECDH Key Exchange

from tinyec import registry
import secrets

curve = registry.get_curve('brainpoolP256r1')


def generate_keypair():
    privKey = secrets.randbelow(curve.field.n)
    pubKey = curve.g * privKey
    return privKey, pubKey


def compress(pubKey):
    return hex(pubKey.x) + hex(pubKey.y % 2)[2:]


def main():
    # Alice generates a random ECC key pair: {alicePrivKey, alicePubKey = alicePrivKey * G}
    alicePrivKey, alicePubKey = generate_keypair()
    print("Alice public key:", compress(alicePubKey))
    # Bob generates a random ECC key pair: {bobPrivKey, bobPubKey = bobPrivKey * G}
    bobPrivKey, bobPubKey = generate_keypair()
    print("Bob public key:", compress(bobPubKey))

    print("Alice and Bob exchange their public keys through the insecure channel (e.g. over Internet)")

    # Alice computes sharedKey: { sharedKey = alicePrivKey * bobPubKey}
    aliceSharedKey = alicePrivKey * bobPubKey
    print("Alice shared key:", compress(aliceSharedKey))

    # same for Bob: { sharedKey = bobPrvKey * alicePubKey }
    bobSharedKey = bobPrivKey * alicePubKey
    print("Bob shared key:", compress(bobSharedKey))

    print("Equal shared keys:", aliceSharedKey == bobSharedKey)


if __name__ == "__main__":
    main()
