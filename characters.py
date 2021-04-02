#Creat class with base specifications

class Human:
    health = 100
    endurance = 100

    def punch(self):
        if endurance > 10:
            return True
        else:
            return False

    def kick(self):
        if endurance > 15:
            return True
        else:
            return False

    def block(self):
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

    def attack(self):
        apperPartBang = 0       #target of attack flag
        lowerPartBang = 0       #target of attack flag
        punch = 0               #type of attack flag
        kick = 0                #type of attack flag

        bang = int(input('Enter 1 for punch or 2 for kick: '))      #type of attack
        target = int(input('Enter 1 for bang head or 2 for bang middle: '))     #target of attack
        if bang == 1:
            if endurance > 10:
                punch += 1
                endurance -= 10
        if bang == 2:
            if endurance > 10:
                kick += 1
                endurance -= 10
        if target == 1:
            apperPartBang += 1
        else:
            lowerPartBang += 1