class Character:
    def __init__(self, charId, name, age, health, atk, speed):
        self.charId = charId
        self.name = name
        self.age = age
        self.health = health
        self.attack = atk
        self.speed = speed

    def __str__(self):
        return f"{self.name}, age: {self.age}"

characters = {}

mary = Character(1, "Mary Poppins", 35, 99, 65, 70)
pooh = Character(2, "Winnie the Pooh", 100, 38, 1, 14)
ness = Character(3, "Ness", 13, 70, 99, 50)

characters[1] = mary
characters[2] = pooh
characters[3] = ness

print(characters[3])