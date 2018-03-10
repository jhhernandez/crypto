#!/usr/bin/env python

import sys

MSGS = ( "hello" )

def strxor(a, b):     # xor two strings of different lengths
  if len(a) > len(b):
    return "".join([chr(ord(x) ^ ord(y)) for (x, y) in zip(a[:len(b)], b)])
  else:
    return "".join([chr(ord(x) ^ ord(y)) for (x, y) in zip(a, b[:len(a)])])

def random(size=16):
  return open("/dev/urandom").read(size)

def encrypt(key, msg):
  c = strxor(key, msg)
  print()
  print(c)
  return c

def main():
  #key = random(1024)
  msg = "attack at dawn"
  cypher = "61747461636b206174206461776e"
  key = strxor(msg, cypher)

  print("msg: " + msg)
  print("cypher: " + cypher)
  print("key: " + key.encode().hex())
  print("reencrypted msg: ")
  encrypt(msg, key)

main()

