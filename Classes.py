# Operator class

class Operator:
    def __init__(self, name, spec, vision, health, attack):
        self.name = name
        self.spec = spec
        self.vision = vision
        self.health = health
        self.maxhealth = health
        self.attack = attack

    def __str__(self):
        return f"Name: {self.name}, Job: {self.spec} Health: {self.health}, Attack: {self.attack}"

    def print_name(self):
        print(self.name)

    def reset(self):
      self.health = self.maxhealth

# Enemy class

class Enemy:
    def __init__(self, name, health, attack, turnstopass):
        self.name = name
        self.health = health
        self.maxhealth = health
        self.attack = attack
        self.turnstopass = turnstopass

    def __str__(self):
        return f"Name: {self.name}, Health: {self.health}, Attack: {self.attack}"

    def print_name(self):
        print(self.name)

    def reset(self):
        self.health = self.maxhealth
