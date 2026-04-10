class Monster:
    def __init__(self, name, hp,dmg):
        self.name = name
        self.hp = hp
        self.dmg = dmg


    def show_info(self):
        print("Имя монстра")
        print(self.name)
        print('-'*10)
        print("Здоровье монстра")
        print(self.hp)
        print('-'*10)
        print("Урон")
        print(self.dmg)

m1 = Monster("Горгулья", 120, 18)
m1.show_info()
