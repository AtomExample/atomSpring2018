class Creature(object):
    def get_sound(self):
        return "Бульк"

class Animal(Creature):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_sound(self):
        return "I'm animal " + super(Animal, self).get_sound()

PER_LIMB_SPEED = 30

class Insect(Creature):
    def __init__(self, limb_count):
        self.limb_count = limb_count
    
    def get_speed(self):
        return self.limb_count * PER_LIMB_SPEED
    
    def get_sound(self):
        return "I'm insect"

class Cocroach(Animal, Insect):

    def get_sound(self):
        return 'Sshh ' + super(Cocroach, self).get_sound()


red = Cocroach(name='Петрович', age=2)
red.limb_count = 8

animal = Animal(name='имя', age=3)
