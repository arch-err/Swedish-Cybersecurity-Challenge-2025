#!/usr/bin/env python

with open("./chall.bin", "rb") as f:
    data = f.read()

# print(data)

blockLength = 16


with open("./solve.bin", "wb") as fs:
    for b in range(0, len(data), blockLength * 2):
        block = data[b : b + blockLength]
        fs.write(block)
        # print(block)
