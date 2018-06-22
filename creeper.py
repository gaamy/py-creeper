import sys
from sys import argv
import random
import subprocess

def main(argv):
  script = argv
  scriptName = str(script[0])
  localCopy(scriptName, 2)
  print("I am the creeper, catch me if you can.")

def localCopy(scriptName,copies):
  for i in range (copies):
    targetName = str(random.randint(1,101))+scriptName
    f = open(targetName,"w+")
    #This is considered a cheat Quine
    #We need to have the whole cource code in a constant (maybe later)
    f.write(open(scriptName).read())
    f.close()

#def remoteCopy():
  


if __name__ == '__main__':
    main(sys.argv)
    exec(__file__+'.py') 
