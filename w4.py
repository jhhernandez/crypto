#!/usr/bin/env python2

import sys

def strxor(a, b):     # xor two strings of different lengths
  if len(a) > len(b):
    return "".join([chr(ord(x) ^ ord(y)) for (x, y) in zip(a[:len(b)], b)])
  else:
    return "".join([chr(ord(x) ^ ord(y)) for (x, y) in zip(a, b[:len(a)])])



s      = "Pay Bob 100$\04\04\04\04"
s1     = "00000000000000003100000000000000".decode('hex')
s2     = "00000000000000003500000000000000".decode('hex')
cipher = "ac1e37bfb15599e5f40eef805488281d"
iv     = "20814804c1767293b99f1d9cab3bc3e7".decode('hex')

print s

bla = strxor(strxor(iv, s1), s2)

print "prev iv: " + iv.encode('hex')
print "curr iv: " + bla.encode('hex')
print "cipher: " + cipher
print "output: " + bla.encode('hex') + cipher
