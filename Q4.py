import matplotlib.pyplot as plt

#Function converting binary to decimal
def ieee_baby(num):
    one = num[0]
    two = num[1:3]
    three = num[3:6]

    if one == '0':
        sign = 1
    else:
        sign = -1
    med = int(two, 2)
    med = 2**(med - 1)
    frac = 0
    if three[0] == '1':
        frac = frac + 0.5
    if three[1] == '1':
        frac = frac + 0.25
    if three[2] == '1':
        frac = frac + 0.125
    frac = 1.0 + frac

    return sign * med * frac


#Calling ieee_baby function
print("IEEE baby decimal value of 010010 is: ", ieee_baby('010010'))


#Part A
babyList = []
for a in range(2):
    for b in range(2):
        for c in range(2):
            for d in range(2):
                for e in range(2):
                    for f in range(2):
                        value = f'{a}{b}{c}{d}{e}{f}'
                        print(value, " ", ieee_baby(value))
                        babyList.append(ieee_baby(value))

totalNum = 0
for element in babyList:
    totalNum = totalNum + 1
print("Total number of unique values: ", totalNum)
#plt.plot(babyList)
#plt.show()

#Part B
#Finding Largest Gap
i = 1
while i < (len(babyList)):
    x = abs(babyList[i] - babyList[i - 1])
    if i == 1:
        bigGap = x
    else:
        if x >= bigGap:
            bigGap = x
    i = i + 1
print("Largest gap size: ", bigGap)
#Finding Smallest Gap
i = 1
while i < (len(babyList)):
    x = abs(babyList[i] - babyList[i - 1])
    if i == 1:
        smallGap = x
    else:
        if x <= smallGap:
            smallGap = x
    i = i + 1
print("Smallest gap size: ", smallGap)
#Smallest Positive Number
posBabyList = []
for element in babyList:
    if element > 0:
        posBabyList.append(element)
smallPos = min(posBabyList)
print("Smallest positive value: ", smallPos)

#Part C
pCount = 0
nCount = 0
for element in babyList:
    if element > 0:
        pCount = pCount + 1
    if element < 0:
        nCount = nCount + 1
if pCount > nCount:
    print ("There are more positive numbers, by ", pCount - nCount)
elif pCount < nCount:
    print("There are more negative numbers, by ", nCount - pCount)
else:
    print("There are the same number of negative and positive numbers")
print("Positive Numbers: ", pCount)
print("Negative Numbers: ", nCount)
