#!/usr/bin/env python3
import sys
import re
from collections import defaultdict
from enum import Enum

signalUnsolvedDict = dict()
signalSolvedDict = dict()

class Signal:
  
  class Operation(Enum):
    AND = 1
    OR = 2
    NOT = 3
    LSHIFT = 4
    RSHIFT = 5
    PASS = 6

  def __init__(self, input1 = None, input2 = None, op = None, value = None):
    self.input1 = None
    self.input2 = None
    self.value = None

    if (input1 != None):
      if (input1.isdigit()): 
        self.input1 = int(input1)
      else:
        self.input1 = input1

    if (input2 != None):
      if (input2.isdigit()): 
        self.input2 = int(input2)
      else:
        self.input2 = input2

    self.op = self.opToEnum(op)
    if (value != None):
      if (value.isdigit()):
        self.value = int(value)
      #else:
      #  self.input1 = value
      #  self.op = self.Operation.PASS

  def updateValue(self, input1, input2):
    if (self.op == self.Operation.AND):
      self.value = input1 & input2
    elif (self.op == self.Operation.OR):
      self.value = input1 | input2
    elif (self.op == self.Operation.NOT):
      self.value = ~input1
    elif(self.op == self.Operation.LSHIFT):
      self.value = input1 << input2
    elif(self.op == self.Operation.RSHIFT):
      self.value = input1 >> input2
    elif(self.op == self.Operation.PASS):
      print( " PASS: " + str(input1))
      self.value = input1


  def __str__(self):
    return str(self.value)
    #str(self.input1) + " " + str(self.op) + " " + str(self.input2) + " -> " + str(self.value)
  def __repr__(self):
    return self.__str__()

  def opToEnum(self, inputString):
    if (inputString == "AND"):
      return self.Operation.AND
    elif (inputString == "OR"):
      return self.Operation.OR
    elif (inputString == "NOT"):
      return self.Operation.NOT
    elif (inputString == "LSHIFT"):
      return self.Operation.LSHIFT
    elif (inputString == "RSHIFT"):
      return self.Operation.RSHIFT
    elif (inputString == "PASS"):
      return self.Operation.PASS

parseRegex = re.compile('([\da-z]*) ?([A-Z]*) ?([\da-z]*) -> ([a-z]*)')

for line in sys.stdin:

  #print(line)
  regexResult = parseRegex.match(line)
  if (regexResult == None):
    print("Parse fail: " + line)
  resultList = list(filter(None, regexResult.groups()))
  #print(resultList)
  if (regexResult == None):
    print( "Failed " + line)
  
  numOperands = len(resultList)
  if (numOperands == 2):
    #Signal Asignment
    if (resultList[0].isdigit()):
      signalSolvedDict[resultList[1]] = Signal(None, None, None, resultList[0])
    else:
      signalUnsolvedDict[resultList[1]] = Signal(resultList[0], None, "PASS")
  elif (numOperands == 3):
    # Single input Gate
    signalUnsolvedDict[resultList[2]] = Signal(resultList[1], None, resultList[0])
  elif (numOperands == 4):
    # two input gate
    signalUnsolvedDict[resultList[3]] = Signal(resultList[0], resultList[2], resultList[1])

while signalUnsolvedDict:
  solvedSignalList = []
  for signalKey, signal in signalUnsolvedDict.items():
    input1 = 0
    input2 = 0

    if (signal.input1 != None):
      if (type(signal.input1) is int):
        input1 = signal.input1
      else:  
        if (signal.input1 in signalSolvedDict):
          input1 = signalSolvedDict[signal.input1].value
        else:
          #print("Input1 Continue")
          continue
    if (signal.input2 != None):
      if (type(signal.input2) is int):
        input2 = signal.input2
      else:  
        if (signal.input2 in signalSolvedDict):
          input2 = signalSolvedDict[signal.input2].value
        else:
          #print("Input2 Continue")
          continue
    print ("Updating " + signalKey + " " + str(signal.op))
    signal.updateValue(input1, input2)

    signalSolvedDict[signalKey] = signal
    solvedSignalList.append(signalKey)

  for key in solvedSignalList:
    signalUnsolvedDict.pop(key)


#print(signalSolvedDict)
#print (" ")
print(signalUnsolvedDict)

print(signalSolvedDict["a"].value)