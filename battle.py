import characters
import ring

battle = ring.Ring()

battle.add(characters.Human, characters.Human)


while battle.fighter1.health > 0 and battle.fighter2.health > 0:
    battle.setPlayers()
    battle.step()
    battle.show()
if battle.fighter1.health == 0:
    print('Fighter 1 lose')
if battle.fighter2.health == 0:
    print('Fighter 2 lose')