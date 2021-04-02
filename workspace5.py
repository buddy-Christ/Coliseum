endurance = 100
print("Endurance: ", endurance)
apperPart = 0       #defence head flag
lowerPart = 0       #defence middle flag
blocked = int(input('Enter 1 for block head or 2 for block middle: '))
if blocked == 1:
    if endurance > 5:
        apperPart += 1
        endurance -= 5
if blocked == 2:
    if endurance > 5:
        lowerPart += 1
        endurance -= 5
print("Head block: ", apperPart, "\nMiddle block: ", lowerPart, "\nEndurance: ", endurance)
        