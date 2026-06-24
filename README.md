# RSA Cryptosystem — From Scratch
**CS 378: Introduction to Cryptology | University of Kentucky | Spring 2026**

> A ground-up Python implementation of the RSA public-key cryptosystem, including square-and-multiply modular exponentiation, Miller-Rabin primality testing, and the Extended Euclidean Algorithm — operating on 200+ digit integers.

---

## Overview

This project implements the full RSA workflow in Python across four modules — no cryptographic libraries used. All core algorithms are hand-implemented per course requirements:

- **Key Setup**: generates two 100-digit primes, computes n = pq, selects e = 65537, derives private key d via Extended Euclidean Algorithm
- **Encryption**: computes ciphertext c = m^e mod n using square-and-multiply
- **Decryption**: recovers plaintext m = c^d mod n using the same algorithm

---

## Project Structure

```
├── math_tools.py    # Core algorithms: modular exponentiation, EEA, Miller-Rabin, prime generation
├── key_setup.py     # Generates and writes public_key and private_key files
├── encryption.py    # Reads public_key + message, writes ciphertext
├── decryption.py    # Reads public_key + private_key + ciphertext, writes decrypted_message
├── public_key       # n and e (one per line)
├── private_key      # d
├── message          # 180-digit plaintext integer
├── ciphertext       # Encrypted output
└── decrypted_message
```

---

## Algorithms Implemented

### Square-and-Multiply Modular Exponentiation (`math_tools.py`)
Computes x^a mod n in O(log a) multiplications by processing exponent bits right-to-left:
```python
def modular_pow(x, a, n):
    result = 1
    x = x % n
    while a > 0:
        if a & 1:
            result = (result * x) % n
        a >>= 1
        x = (x * x) % n
    return result
```

### Miller-Rabin Primality Test (`is_probable_prime`)
- Decomposes n-1 = 2^s * d
- Runs k=20 independent witness tests
- First filters with small prime trial division for speed
- Returns composite immediately on any witness failure; probabilistic prime otherwise

### Large Prime Generation (`generate_prime`)
- Generates random k-digit integers in range [10^(k-1), 10^k - 1]
- Forces odd, then tests with Miller-Rabin
- Loops until a probable prime is found

### Extended Euclidean Algorithm (`egcd`, `modinv`)
Recursive EEA returns (gcd, x, y) satisfying ax + by = gcd(a,b). Used to compute d = e^-1 mod φ(n).

### Key Generation (`key_setup.py`)
- Generates p and q with ≥100 decimal digits each
- Enforces |p - q| ≥ 10^95 to prevent factoring attacks
- Uses e = 65537 (standard choice; verified coprime with φ(n))
- Derives d = modinv(e, φ(n))

---

## Usage

```bash
# Step 1: Generate keys
python3 key_setup.py
# → writes public_key and private_key

# Step 2: Encrypt a message
# message file must contain an integer ≥ 150 digits and < n
python3 encryption.py
# → writes ciphertext

# Step 3: Decrypt
python3 decryption.py
# → writes decrypted_message
```

---

## Test Run

Plaintext (180-digit integer):
```
777777777777777000000000000000222222222222222333333333333333444444444444444222222222222222555555555555555666666666666666777777777777777888888888888888999999999999999000000000000000
```

Verified: `decrypted_message == message` ✓

---

## Key Properties

| Property | Value |
|---|---|
| Key size | ~200 decimal digits (~664 bits) |
| Prime size | 100 decimal digits each |
| Public exponent e | 65537 |
| Primality test | Miller-Rabin, k=20 rounds |
| Exponentiation | Square-and-multiply, O(log e) |
| Inverse computation | Extended Euclidean Algorithm |

---

## Environment
- Language: Python 3
- No external crypto libraries — all algorithms hand-implemented
- Course: CS 378 Introduction to Cryptology, University of Kentucky
