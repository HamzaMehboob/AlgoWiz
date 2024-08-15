# Hashing Algorithms Collection

This repository contains Python implementations of various cryptographic and non-cryptographic hashing algorithms. Below is a brief description of each algorithm and the corresponding script.

## Table of Contents

1. [BLAKE2](#blake2)
2. [BLAKE3](#blake3)
3. [FNV-1a](#fnv-1a)
4. [MD4](#md4)
5. [MurmurHash3 (MMH3)](#murmurhash3-mmh3)
6. [PBKDF2](#pbkdf2)
7. [RIPEMD-160](#ripemd-160)
8. [SHA-1](#sha-1)
9. [SHA-3 (SHA3-256)](#sha-3-sha3-256)
10. [SHA-256](#sha-256)
11. [SHA-512](#sha-512)
12. [XXHash](#xxhash)
13. [CRC32 (zlib)](#crc32-zlib)

---

## BLAKE2

- **Script:** `blake2.py`
- **Description:** BLAKE2 is a cryptographic hash function designed as a faster secure alternative to MD5 and SHA-2. It is optimized for performance and security.

## BLAKE3
- **Script:** `blake3Algo.py`
- **Description:**  BLAKE3 is a cryptographic hash function that combines the security of BLAKE2 with higher speed and parallelism.

## FNV-1a
- **Script:** `fnv1a.py`
- **Description:** FNV-1a is a non-cryptographic hash function with good distribution and performance, commonly used in hash tables.

## MD4
- **Script:** `md4.py`
- **Description:** MD4 is a cryptographic hash function that produces a 128-bit hash value. It is considered insecure for modern applications.

## MurmurHash3 (MMH3)
- **Script:** `mh3Hash.py`
- **Description:** MurmurHash3 is a non-cryptographic hash function known for its excellent distribution qualities and performance.

## PBKDF2
- **Script:** `pbkdf2.py`
- **Description:** PBKDF2 (Password-Based Key Derivation Function 2) is a key derivation function with a sliding computational cost, used to reduce brute-force attacks on stored passwords.

## RIPEMD-160
- **Script:** `ripemd160.py`
- **Description:** RIPEMD-160 is a cryptographic hash function producing a 160-bit hash value, commonly used in blockchain technologies.

## SHA-1
- **Script:** `sha1.py`
- **Description:** SHA-1 is a cryptographic hash function producing a 160-bit hash value. It is considered insecure for most applications due to vulnerability to collision attacks.

## SHA-3 (SHA3-256)
- **Script:** `sha3_256.py`
- **Description:** SHA3-256 is part of the SHA-3 family of cryptographic hash functions, producing a 256-bit hash value.

## SHA-256
- **Script:** `sha256.py`
- **Description:** SHA-256 is a cryptographic hash function producing a 256-bit hash value, commonly used in blockchain and security applications.

## SHA-512
- **Script:** `sha512.py`
- **Description:** SHA-512 is a cryptographic hash function producing a 512-bit hash value, offering a higher level of security than SHA-256.

## XXHash
- **Script:** `xxhashAlgo.py`
- **Description:** XXHash is an extremely fast non-cryptographic hash function with excellent distribution properties, ideal for high-performance hashing.

## CRC32 (zlib)
- **Script:** `zlib.py`
- **Description:** CRC32 is a non-cryptographic hash function used primarily for error-checking in data transmission.