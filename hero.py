class SuperHero:
    people = 'people'
    def __init__ (self,name,nickname,superpower,health_points,catchphrase):
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

Hero = SuperHero('Bruce Wayne', 'Batman', 'Money and power', 1000, 'I am Batman!')

print(Hero)
print(Hero.name)
Hero.age_multiplier()
print(len(Hero))
