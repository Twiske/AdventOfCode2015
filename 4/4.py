#!/usr/bin/env python3
import hashlib


puzzleInput = "iwrupvqb"

addition = 1000
while (True):
  hashString = puzzleInput + format(addition,'d')
  #print(hashString.encode('utf-8'))
  m = hashlib.md5()
  m.update(hashString.encode('utf-8'))
  output = m.hexdigest()


  if (len(output) - len(output.lstrip('0')) == 6):
    print(hashString)
    print(output)
  #print(output.lstrip('0'))
    break
  addition += 1
