#!/usr/bin/env python3
import sys
import re

dim = 1000

rangeRegex = re.compile('(\\d*),(\\d*) through (\\d*),(\\d*)')

lightArray = [[0 for x in range(dim)] for x in range(dim)]

for line in sys.stdin:
  rangeResult = rangeRegex.search(line)

  x1 = int(rangeResult.groups()[0])
  y1 = int(rangeResult.groups()[1])

  x2 = int(rangeResult.groups()[2])
  y2 = int(rangeResult.groups()[3])

#  print(rangeResult.groups())
  for x in range(x1, x2+1):
    for y in range(y1, y2+1):
      if (line[6] == 'n'):
        lightArray[x][y] += 1
      elif (line[6] == 'f'):
        lightArray[x][y] -= 1
        if (lightArray[x][y] < 0):
          lightArray[x][y] = 0
      else:
        lightArray[x][y] += 2
      
totalLights = sum(map(sum, lightArray))
print(totalLights)
