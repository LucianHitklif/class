class Zombie:
    def __init__(self, name, hp):
        self.name = name
        self.hp = hp

    def bite(self, damage):
        self.hp -= damage
        return self.hp


m1 = Zombie('Мясник', 100)

damage = int(input("Введите силу укуса: "))
res = m1.bite(damage)

print(f"Остаток здоровья: {res}")
