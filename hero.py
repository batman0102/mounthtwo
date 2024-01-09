class SuperHero:
    people = 'people'
    def __init__ (self, name, nickname, superpower, health_points, catchphrase):
        self.name = name
        self.nickname = nickname
        self.superpower = superpower
        self.health_points = health_points
        self.catchphrase = catchphrase

    def name(self):
        print(self.name)

    def age_multiplier(self):
        print(self.health_points * 2)

    def __str__(self):
        return f'nickname: {self.nickname}, health_points: {self.health_points}, superpower: {self.superpower}'

    def __len__(self):
        return len(self.catchphrase)

Hero = SuperHero('Bruce Wayne', 'Batman', \
       'Money and power', 800, 'I am Batman!')


# print(Hero)
# print(Hero.name)
# Hero.age_multiplier()
# print(len(Hero))

class SuperHero2(SuperHero):
    people = 'people'

    def __init__(self, name, nickname, superpower, health_points, catchphrase, damage, fly = False):
        super().__init__(name, nickname, superpower, health_points, catchphrase)
        self.damage = damage
        self.fly = fly
    def age_exponent(self):
        print (self.health_points ** 2)
        self.fly = True

    def __str__(self):
        return f'nickname: {self.nickname}, health_points: {self.health_points}, \
superpower: {self.superpower}, damage: {self.damage}, can fly: {self.fly}'
    def phrase(self):
        return 'True in the True_phrase'

Hero2 = SuperHero2('Кларк Кент', 'Superman',\
                   'Eyes and power', 1000,\
                   'Truth, Justice and the American Way',\
                   999, True)
Hero2.age_exponent()
print(Hero2)
print(Hero2.phrase())


class SuperHero3(SuperHero):
    people = 'people'

    def __init__(self, name, nickname, superpower, health_points, catchphrase, damage, fly = False):
        super().__init__(name, nickname, superpower, health_points, catchphrase)
        self.damage = damage
        self.fly = fly

    def age_exponent(self):
        print (self.health_points ** 2)
        self.fly = True

    def phrase(self):
        return 'True in the True_phrase'

    def __str__(self):
        return f'nickname: {self.nickname}, health_points: {self.health_points}, \
superpower: {self.superpower}, damage: {self.damage}, can fly: {self.fly}'


Hero3 = SuperHero3('Джексон Хайд', 'Aquaman', 'Water',\
                   600, "I am Aquaman.", 200, False)

Hero3.age_exponent()
print(Hero3)
print(Hero3.phrase())

class Villain(SuperHero3):
    people = 'monster'

    def gen_x(self):
        pass

    def crit(self):
        print(self.damage ** 2)

Monster = Villain('Танос', 'Thanos', 'Telepathy', \
                  1000, 'Reality can be whatever I want it to be!', 400, False)

Villain.crit(Hero3)