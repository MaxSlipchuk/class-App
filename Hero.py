
class Hero():
    def __init__(self, name, health, weapon, damage):
        self.name = name
        self.health = health
        self.weapon = weapon
        self.damage = damage

    def atack(self, other_player):
        damage = self.damage
        print(f"{self.name} attacked {other_player} and dealt {damage} damage.")
        other_player.take_damage(damage)

    def take_damage(self, damage):
        damage = self.damage
        self.health -= damage
        print(f"{self.name} took {damage} damage. Health remaining: {self.health}")

    def print_info(self):
        print("Ім`я маг", self.name)
        print("Здоров`я", self.health)
        print("Зброя", self.weapon)
        print("Урон", self.damage)

magik_man = Hero("Gendalf", 80, "book", 30) 
gun_man = Hero("Kuri", 100, "mini_gun", 20)

magik_man.atack(gun_man)

magik_man.print_info()
print()
gun_man.print_info()

