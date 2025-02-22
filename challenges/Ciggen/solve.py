#!/usr/bin/env python
import os
import ecdsa
import secrets
import hashlib
from sympy import symbols, solve

gen = ecdsa.NIST256p.generator
order = gen.order()


def H(m):
    return int.from_bytes(hashlib.sha256(m).digest(), "big") % order


r1 = 75500473885933440102349250800371371719844218835306589569739362373352510711748
s1 = 16024164171116223134077765902232407130958988685148352157522953597450963414049
r2 = 75500473885933440102349250800371371719844218835306589569739362373352510711748
s2 = 4694071681235633686740348059417161949764482691159381333680771208497833303204

h1 = H(b":)")
h2 = H(b":O")

k = symbols("k")

poly1 = 6 * k**17 + 13 * k - 3 * k**17 - 20 * k - 3 * k**17 + 8 * k
poly2 = 15 * k**13 - 16 * k - 23 * k**13 + 12 * k + 8 * k**13 + 5 * k

# ECDSA signature equations:
# s1 = k^-1 * (h1 + d * r1) mod order
# s2 = k^-1 * (h2 + d * r2) mod order

# Since r1 == r2, we can eliminate d:
# s1 * k = h1 + d * r1
# s2 * k = h2 + d * r1
# d = (s1 * k - h1) / r1
# d = (s2 * k - h2) / r1
# s1 * k - h1 = s2 * k - h2
# k * (s1 - s2) = h1 - h2
# k = (h1 - h2) * pow(s1 - s2, -1, order)

k_val = (h1 - h2) * pow(s1 - s2, -1, order) % order

# Recover private key d:
d = (s1 * k_val - h1) * pow(r1, -1, order) % order

# Extract the flag:
d_bytes = d.to_bytes((d.bit_length() + 7) // 8, "big")
flag = d_bytes[2:].split(b"\0", 1)[0]

print(f"{flag=}")
