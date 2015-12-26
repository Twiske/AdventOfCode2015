#!/usr/bin/env python3
from collections import defaultdict

import sys


class Point:
  x = 0
  y = 0

  def __str__(self):
    return "X:" + str(self.x) + " Y:" + str(self.y)

  def __hash__(self):
    return hash((self.x, self.y))

  def __eq__(self, other):
    if (self.x == other.x and self.y == other.y):
      return true
    else:
      return false
    #return (self.x, self.y) == (other.x, other.y)

  def __ne__(self, other):
    return not self == other

currentLocation = Point()
currentLocationRobo = Point()

#visitList = defaultdict(int)
visitList = [(0,0)]
totalHouses = 1

#visitList[currentLocation] += 1

index = 0
for line in sys.stdin:
  for character in line:
    if (index % 2 == 0):
      if (character == '^'):
        currentLocation.y += 1
      elif (character == 'v'):
        currentLocation.y -= 1
      elif (character == '>'):
        currentLocation.x += 1
      elif (character == '<'):
        currentLocation.x -= 1
    else:
      if (character == '^'):
        currentLocationRobo.y += 1
      elif (character == 'v'):
        currentLocationRobo.y -= 1
      elif (character == '>'):
        currentLocationRobo.x += 1
      elif (character == '<'):
        currentLocationRobo.x -= 1

    #visitList[currentLocation] += 1
    index += 1

    if ((currentLocation.x, currentLocation.y) not in visitList):
      totalHouses += 1
      visitList.append((currentLocation.x, currentLocation.y))
    if ((currentLocationRobo.x, currentLocationRobo.y) not in visitList):
      totalHouses += 1
      visitList.append((currentLocationRobo.x, currentLocationRobo.y))

#print(visitList)
#print (len(visitList))
print(totalHouses)
