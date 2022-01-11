import random

throwings = []
sum = 0
fourCount = 0
evenNumIndexes = []
numDistribution = [0, 0, 0, 0, 0, 0]
actualIndex = 1
hasPattern = 'false'

while sum < 100:
  actualNumber = random.randint(1, 6)
  if sum + actualNumber <= 100:
    throwings.append(actualNumber)
    numDistribution[actualNumber-1] = numDistribution[actualNumber-1] + 1
    sum += actualNumber
    if actualNumber == 4:
      fourCount+=1
    if actualNumber % 2 == 0:
      evenNumIndexes.append(actualIndex)
    actualIndex += 1
    if actualIndex > 5:
      if throwings[actualIndex - 2] == 5 and throwings[actualIndex - 3] == 4 and throwings[actualIndex - 4] == 3 and throwings[actualIndex - 5] == 2 and throwings[actualIndex - 6] == 1:
        hasPattern = 'true'

maxNum = max(numDistribution)

print("Dobások:", throwings)
print("Összeg:", sum)
print("4-es darab:", fourCount)
print("Páros indexek:", evenNumIndexes)
for i in range(6):
    print(i+1,"-", numDistribution[i], "darab")
print("Legtöbbször előfordul: ", end="")
for i in range(6):
    if numDistribution[i] == maxNum:
      print(i+1, end=" ")
if hasPattern == 'true':
  print("\nVan benne 1, 2, 3, 4, 5, 6 sorozat.")
else:
  print("\nNincs benne 1, 2, 3, 4, 5, 6 sorozat.")