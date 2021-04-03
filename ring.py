import characters

class Ring:
    exchange = 1        #one of the iterations attacks and blocks
    fighter1 = None         #fighter which fight
    fighter2 = None         #fighter which fight

    def add(self, fighter1Class, fighter2Class):
        self.fighter1 = fighter1Class()
        self.fighter2 = fighter2Class()


    def infoPlayers(self, fighter, number):
        attackTypePlayer = int(input('{0} Enter 1 for punch or 2 for kick Player : '.format(number)))      #type of attack
        attackTargetPlayer = int(input('{0} Enter 1 for bang head or 2 for bang middle Player : '.format(number)))     #target of attack
        blockPlayer = int(input('{0} Enter 1 for block head or 2 for block middle Player : '.format(number)))
        fighter.block(blockPlayer)
        fighter.attack(attackTypePlayer, attackTargetPlayer)

    def setPlayers(self):
        self.infoPlayers(self.fighter1, 1)
        self.infoPlayers(self.fighter2, 2)



    def step(self):
        #attack fighter1 in head
        if self.fighter2.blocked() == 2 and self.fighter1.headBang == 1:
            if self.fighter1.punch ==1 :
                self.fighter2.health -= 10
            if self.fighter1.kick == 2:
                self.fighter2.health -= 20
        #attack fighter2 in head
        if self.fighter1.blocked() == 2 and self.fighter2.headBang == 1:
            if self.fighter2.punch == 1:
                self.fighter1.health -= 10
            if self.fighter2.kick == 2:
                self.fighter1.health -= 20
        #attack fighter 1 in middle
        if self.fighter2.blocked() == 1 and self.fighter1.middleBang == 2:
            if self.fighter1.punch == 1:
                self.fighter2.health -= 10
            if self.fighter1.kick == 2:
                self.fighter2.health -= 20
        #attack fighter 2 in middle
        if self.fighter1.blocked() == 1 and self.fighter2.middleBang == 2:
            if self.fighter2.punch == 1:
                self.fighter1.health -= 10
            if self.fighter2.kick == 2:
                self.fighter1.health -= 20


    def show(self):
        print('\n',self.fighter1.show(),'\n', self.fighter2.show())