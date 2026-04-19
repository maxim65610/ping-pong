class Hero():
    def __init__(self, name, health, armor):
        self.name = name
        self.health = health
        self.armor = armor
    def printinfo(self):
        print('Имя - ', self.name)
        print('Здоровье - ', self.health)
        print('Броня - ', self.armor)

hero1 = Hero('Вася', 50, 50)