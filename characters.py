#Create class with base specifications

class Human:
    health = 50
    endurance = 100
    __blocked = 0
    headBang = 0       #target of attack flag
    middleBang = 0       #target of attack flag
    punch = 0               #type of attack flag
    kick = 0                #type of attack flag


    def blocked(self):      #getter
        return self.__blocked


    def block(self, blocked):       #setter
        self.__blocked = 0
        if blocked == 1 or blocked == 2:            #1 for head block and 2 for middle block
            if self.endurance > 5:
                self.endurance -= 5
                self.__blocked = blocked


    def attack(self, typeAttack, targetAttack):
        self.headBang = 0
        self.middleBang = 0
        self.punch = 0
        self.kick = 0
        if self.endurance > 10:
            if typeAttack == 1:
                self.endurance -= 5
                self.punch = typeAttack
            if typeAttack == 2:
                self.endurance -= 10
                self.kick = typeAttack
            if targetAttack == 1:
                self.headBang = targetAttack
            if targetAttack == 2:
                self.middleBang = targetAttack

    def show(self):
        return 'Health: {0} Endurance: {1} Block: {2}'.format(self.health, self.endurance, self.blocked())
