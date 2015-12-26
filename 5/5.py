#!/usr/bin/env python3
import re
import sys

badList = ["ab", "cd", "pq", "xy"]

double = re.compile('(.)\\1{1,}')
vowel = re.compile('[aeiou]')

numNiceStrings = 0
for line in sys.stdin:
  if any(substring in line for substring in badList):
    print("BAD: bad pattern")
    continue

  doubleResult = double.search(line)
  #print(doubleResult)
  if doubleResult is None:
    print("BAD: no double")
    continue

  vowelResult = vowel.findall(line)
  if len(vowelResult) < 3:
    print("BAD: <3 vowels")
    continue
  
  print("GOOD")
  numNiceStrings += 1

print(numNiceStrings)