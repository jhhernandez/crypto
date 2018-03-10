#!/usr/bin/python

import sys

MSGS = [
    "315c4e",
    "234c02",
    "32510b",
    "32510b",
    "3f561b",
    "32510b",
    "32510b",
    "315c4e",
    "271946",
    "466d06"
]

def buf_xor(a, b): # xor two buffers of different lengths
    arr = bytearray()
    if len(a) > len(b):
        for (x, y) in zip(a[:len(b)], b): arr.append(x ^ y)
    else:
        for (x, y) in zip(a, b[:len(a)]): arr.append(x ^ y)
    return arr

def main():
    MSGS_BUF = []
    results = []
    for msg in MSGS:
        MSGS_BUF.append(bytearray.fromhex(msg))

    max_len = len(max(MSGS_BUF, key = len))
    key = bytearray(max_len)

    for i, m1 in enumerate(MSGS_BUF):
        for j in range(i + 1, len(MSGS_BUF)):
            results.append((i, j, buf_xor(m1, MSGS_BUF[j])))
            j = j + 1

    for i, res in enumerate(results):
        j, k, msg = res

        # print('j: {0} k: {1} xor: {2}'.format(j, k, msg.hex()))

        for l, byte in enumerate(msg):
            if byte == 32 and MSGS_BUF[j][l] < 128:
                print('inserting {0} in position {1}'.format(byte, l))
                key[l] = byte

    print('key: ' + key.hex())

    for msg in MSGS_BUF:
        xor = buf_xor(msg, key)
        print(xor)

main()
