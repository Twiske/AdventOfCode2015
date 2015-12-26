#!/usr/bin/env python3
import re
import sys


pair = re.compile('(..).*?\\1')
singleSpace = re.compile('(.).\\1')

numNiceStrings = 0
for line in sys.stdin:
  doubleResult = pair.search(line)
  #print(doubleResult)
  if doubleResult is None:
    print("BAD: no pair")
    continue

  spaceResult = singleSpace.search(line)
  if spaceResult is None:
    print("BAD: no xax")
    continue
  
  print("GOOD")
  numNiceStrings += 1

print(numNiceStrings)