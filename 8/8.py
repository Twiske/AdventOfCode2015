#!/usr/bin/env python3
import sys
import re

stringRegex = re.compile('"(.*?)"')

for line in sys.stdin:
  internalString = stringRegex.search(line).groups()[0]
  processedString = bytes(internalString, "utf-8").decode("unicode_escape")
  print(len(processedString))
  print(len(line))
  #print(len(raw(line)))