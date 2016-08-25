accList = []
accIndex = []

while 1:
    buff = float(raw_input())
    if buff == 100:
        break

    accList.append(buff)

for index in range(1, len(accList) - 1):
    if accList[index] >= accList[index - 1] and accList[index] > accList[index + 1] and accList[index] > 0:
        accIndex.append(index)

print
print
timeList = []
lowerTime = float(raw_input())
upperTime = float(raw_input())

while lowerTime <= upperTime:
    timeList.append(lowerTime)
    lowerTime += 0.02

print
print

timeStart = float(raw_input())

print
print

for num in accIndex:
    print accList[num]

print

for num in accIndex:
    print timeList[num] - timeStart
