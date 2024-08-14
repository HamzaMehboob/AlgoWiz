from ecc import ECCCrypto

# Initialize ECC
ecc = ECCCrypto()

# Message to be signed
message = "This is a secret message"

# Sign the message
signature = ecc.sign(message)
print(f"Signature: {signature}")

# Get the public key
public_key = ecc.get_public_key()
print(f"Public Key: {public_key}")

# Verify the signature with the public key
is_verified = ecc.verify(message, signature, public_key)
print(f"Signature Verified: {is_verified}")
