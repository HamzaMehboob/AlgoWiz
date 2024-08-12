from diffie_hellman import DiffieHellman

if __name__ == "__main__":
    # Alice generates her keys
    alice = DiffieHellman()
    alice_public_key = alice.get_public_key()
    p, g = alice.get_params()

    # Bob generates his keys
    bob = DiffieHellman()
    bob_public_key = bob.get_public_key()

    # Exchange public keys
    alice_shared_key = alice.generate_shared_key(bob_public_key)
    bob_shared_key = bob.generate_shared_key(alice_public_key)

    # Both shared keys should be the same
    print("Alice's Shared Key:", alice_shared_key)
    print("Bob's Shared Key:", bob_shared_key)
