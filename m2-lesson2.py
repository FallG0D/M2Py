class cars:
    position = '0'
    move = 0

    def __init__(self,name='Unknown',beep='silence...', power='0'):
        self.name = name
        self.beep = beep
        self.power = power

    def beep(self):
        print(self.beep)

    def position_(self):
        print(self.position)

    def move_(self):
        self.move += 1
        print(self.move)


car = cars(name='Lexus', beep='on', power='265')
car.name()
car.beep()
car.power()


